/* La scène du thème, la même que sur l'accueil : dessinée une fois, immobile. */
import {createCosmos} from './univers-scene.mjs?v=__SCENE_VERSION__';

const figure = document.querySelector('.scene-sujet');
if (figure) {
  const scene = Number(figure.dataset.scene);
  const cosmos = createCosmos(figure.querySelector('canvas'), {
    count: matchMedia('(max-width: 760px)').matches ? 9000 : 22000, cadrage: 'centre',
  });
  const dessiner = () => { cosmos.resize(); cosmos.draw({from: scene, to: scene, blend: 1}); };
  new ResizeObserver(dessiner).observe(cosmos.canvas);
  document.documentElement.classList.add('scene-js');
}
