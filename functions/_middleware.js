// Envoie chaque visiteur vers la version de sa langue (en-tête Accept-Language),
// l'anglais pour les langues non traduites.
// Ne s'exécute que sur les chemins sans préfixe de langue (voir public/_routes.json).
// Langues publiées : les 11 langues du site (site/langues/<code>.py).
const LANGUES = ['fr', 'en', 'es', 'de', 'it', 'pt', 'ru', 'zh', 'ja', 'ko', 'ar'];
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
  if (LANGUES.includes(url.pathname.split('/')[1])) return next();
  url.pathname = `/${choisir(request)}${url.pathname}`;
  return new Response(null, {
    status: 302,
    headers: { Location: url.toString(), Vary: 'Accept-Language', 'Cache-Control': 'private, no-store' },
  });
}
