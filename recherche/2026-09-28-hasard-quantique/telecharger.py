#!/usr/bin/env python3
"""aeternam, test n° 4 : reconstruit donnees/ à partir des sources primaires.

Les fichiers de donnees/ sont déjà dans le dépôt (chacun < 5 Mo) ; ce script
montre d'où ils viennent et permet de les refaire. Il télécharge :

  1. Parity QRNG (Kavulich, Van Deren, Schlosshauer, Phys. Lett. A 388, 127032,
     2021), Zenodo 10.5281/zenodo.4440318, parity.zip (133 Mo, md5 publié par
     Zenodo). Chaque fichier parity_k contient la chaîne unique k de 64 000 bits
     (8 000 octets) répétée en boucle : on garde les 8 000 premiers octets de
     parity_1 ... parity_100 -> 6 400 000 bits bruts, sans post-traitement.
  2. IBM, « Basic QRNG » (Root et Becker, arXiv:2401.12250), Zenodo
     10.5281/zenodo.10542216, S_2023_trials.zip (33 Mo) : fichiers
     combined_sequences/combined_Basic_QRNG_<machine>.txt (caractères 0/1),
     compactés 8 bits par octet, dans l'ordre de MACHINES_IBM.
  3. ANU QRNG (même dépôt Zenodo que 1), ANU.zip (21 Go) : on ne lit par
     requête HTTP Range que le début du premier membre (anubits_1, compressé
     deflate) et on en garde les 2 097 152 premiers octets décompressés.
  4. NIST Randomness Beacon 2.0, chaîne 2, impulsions 1 950 000 à 1 958 191 :
     localRandomValue (64 octets) puis precommitmentValue (64 octets) par
     impulsion, via https://beacon.nist.gov/beacon/2.0/chain/2/pulse/<i>.

Chaque fichier produit est comparé à l'empreinte SHA-256 inscrite dans
analyse.py. Usage : python3 telecharger.py [--cache DOSSIER]
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import json
import struct
import time
import urllib.request
import zipfile
import zlib
from pathlib import Path

import numpy as np

import analyse

ZENODO_KS = 'https://zenodo.org/api/records/4440318/files/{}/content'
ZENODO_IBM = 'https://zenodo.org/api/records/10542216/files/S_2023_trials.zip/content'
MD5 = {'parity.zip': '9dd06b096f135f067d8e6af30b446c13',
       'S_2023_trials.zip': 'c76329c507922b97b3ce0a9b67162610'}
BEACON = 'https://beacon.nist.gov/beacon/2.0/chain/2/pulse/{}'


def telecharger(url: str, dest: Path, md5: str) -> Path:
    if not dest.exists() or hashlib.md5(dest.read_bytes()).hexdigest() != md5:
        print('téléchargement', url)
        urllib.request.urlretrieve(url, dest)
    assert hashlib.md5(dest.read_bytes()).hexdigest() == md5, dest
    return dest


def parity(cache: Path) -> bytes:
    z = zipfile.ZipFile(telecharger(ZENODO_KS.format('parity.zip'), cache / 'parity.zip', MD5['parity.zip']))
    morceaux = []
    for k in range(1, 101):
        with z.open(f'parity_{k}') as f:
            d = f.read(3 * 8000)
        assert d[:8000] == d[8000:16000] == d[16000:], f'parity_{k} : période différente de 64 000 bits'
        morceaux.append(d[:8000])
    return b''.join(morceaux)


def ibm(cache: Path) -> bytes:
    z = zipfile.ZipFile(telecharger(ZENODO_IBM, cache / 'S_2023_trials.zip', MD5['S_2023_trials.zip']))
    out = []
    for m in analyse.MACHINES_IBM:
        s = z.read(f'S_2023_trials/combined_sequences/combined_Basic_QRNG_{m}.txt')
        a = np.frombuffer(s, np.uint8) - 48
        assert set(np.unique(a)) <= {0, 1} and len(a) % 8 == 0
        out.append(np.packbits(a).tobytes())
    return b''.join(out)


def anu() -> bytes:
    n = analyse.OCTETS_ANU
    req = urllib.request.Request(ZENODO_KS.format('ANU.zip'), headers={'Range': f'bytes=0-{n + (1 << 20)}'})
    brut = urllib.request.urlopen(req, timeout=600).read()
    sig, _, _, meth, _, _, _, _, _, ln, le = struct.unpack('<IHHHHHIIIHH', brut[:30])
    assert sig == 0x04034B50 and meth == 8 and brut[30:30 + ln] == b'anubits_1'
    sortie = zlib.decompressobj(-15).decompress(brut[30 + ln + le:], n)
    assert len(sortie) == n
    return sortie


def beacon() -> bytes:
    def une(i):
        for essai in range(8):
            try:
                p = json.load(urllib.request.urlopen(BEACON.format(i), timeout=60))['pulse']
                assert p['pulseIndex'] == i and p['cipherSuite'] == 0
                return bytes.fromhex(p['localRandomValue']) + bytes.fromhex(p['precommitmentValue'])
            except Exception:
                time.sleep(2 + 3 * essai)
        raise SystemExit(f'impulsion {i} inaccessible')
    debut, n = analyse.BEACON_PREMIERE, analyse.BEACON_NOMBRE
    with cf.ThreadPoolExecutor(6) as ex:
        return b''.join(ex.map(une, range(debut, debut + n)))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cache', type=Path, default=Path('/tmp/aeternam-hasard'))
    ap.add_argument('--sortie', type=Path, default=analyse.DONNEES)
    args = ap.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    args.sortie.mkdir(parents=True, exist_ok=True)
    fabriques = {'parity_qrng.bin': lambda: parity(args.cache), 'ibm_basic_qrng.bin': lambda: ibm(args.cache),
                 'anu_qrng.bin': anu, 'nist_beacon.bin': beacon}
    for nom, fab in fabriques.items():
        d = fab()
        emp = hashlib.sha256(d).hexdigest()
        attendu = analyse.FICHIERS[nom]['sha256']
        (args.sortie / nom).write_bytes(d)
        print(nom, len(d), emp, 'OK' if emp == attendu else f'DIFFÉRENT (attendu {attendu})')


if __name__ == '__main__':
    main()
