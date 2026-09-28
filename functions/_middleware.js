// Envoie chaque visiteur vers la version de sa langue (en-tête Accept-Language) :
// français si le navigateur le préfère, anglais sinon.
// Ne s'exécute que sur les chemins sans préfixe de langue et sur les anciennes
// langues retirées (voir public/_routes.json).
const LANGUES = ['fr', 'en'];
// Langues publiées jusqu'au 28 septembre 2026 : leurs adresses redirigent durablement.
const RETIREES = ['es', 'de', 'it', 'pt', 'ru', 'zh', 'ja', 'ko', 'ar'];
const DEFAUT = 'en';

function choisir(request) {
  const preferences = (request.headers.get('Accept-Language') || '')
    .split(',')
    .map((partie, rang) => {
      const [etiquette, ...parametres] = partie.trim().split(';');
      const q = parametres.map((p) => p.trim()).find((p) => p.startsWith('q='));
      return { code: etiquette.trim().toLowerCase().split('-')[0], q: q ? Number(q.slice(2)) : 1, rang };
    })
    .filter((p) => p.code && p.q > 0)
    .sort((a, b) => b.q - a.q || a.rang - b.rang);
  const trouvee = preferences.find((p) => LANGUES.includes(p.code));
  return trouvee ? trouvee.code : DEFAUT;
}

export async function onRequest({ request, next }) {
  const url = new URL(request.url);
  const premier = url.pathname.split('/')[1];
  if (LANGUES.includes(premier)) return next();
  let status = 302;
  if (RETIREES.includes(premier)) {
    url.pathname = url.pathname.slice(premier.length + 1) || '/';
    status = 301;
  }
  url.pathname = `/${choisir(request)}${url.pathname}`;
  return new Response(null, {
    status,
    headers: { Location: url.toString(), Vary: 'Accept-Language', 'Cache-Control': 'private, no-store' },
  });
}
