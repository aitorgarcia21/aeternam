/** Modèles pédagogiques explicites, sans dépendance au rendu ou à la cadence. */
export const CRITICAL_IMPACT = 3 * Math.sqrt(3) / 2;

export function movingClockRatio(beta) {
  if (!Number.isFinite(beta) || Math.abs(beta) >= 1) throw new RangeError('La vitesse doit rester inférieure à c.');
  return Math.sqrt(1 - beta * beta);
}

export function stationaryClockRatio(radius) {
  if (!Number.isFinite(radius) || radius <= 1) throw new RangeError('Une horloge stationnaire doit rester à r > rₛ.');
  return Math.sqrt(1 - 1 / radius);
}

export function traceLight(impact, step = 0.002) {
  if (!Number.isFinite(impact) || impact <= 0 || !Number.isFinite(step) || step <= 0) throw new RangeError('Paramètres de géodésique invalides.');
  // u = r_s/r ; u(0) = 0 à l'infini ; u'(0) = 1/b.
  const acceleration = u => -u + 1.5 * u * u;
  const points = [];
  let u = 0, v = 1 / impact, phi = 0, closest = Infinity;
  for (let i = 0; i < Math.ceil(24 / step); i++) {
    const u0 = u, phi0 = phi;
    const k1u = v, k1v = acceleration(u);
    const k2u = v + step * k1v / 2, k2v = acceleration(u + step * k1u / 2);
    const k3u = v + step * k2v / 2, k3v = acceleration(u + step * k2u / 2);
    const k4u = v + step * k3v, k4v = acceleration(u + step * k3u);
    u += step * (k1u + 2 * k2u + 2 * k3u + k4u) / 6;
    v += step * (k1v + 2 * k2v + 2 * k3v + k4v) / 6;
    phi += step;
    if (u >= 1) {
      const at = phi0 + step * (1 - u0) / (u - u0);
      points.push([-Math.cos(at), Math.sin(at)]);
      return {points, captured: true, escaped: false, closest: 1, deflection: null};
    }
    if (u <= 0) {
      const at = phi0 + step * u0 / (u0 - u);
      return {points, captured: false, escaped: true, closest, deflection: at - Math.PI};
    }
    const r = 1 / u;
    closest = Math.min(closest, r);
    if (r < 32) points.push([-r * Math.cos(phi), r * Math.sin(phi)]);
  }
  return {points, captured: false, escaped: false, closest, deflection: null};
}
