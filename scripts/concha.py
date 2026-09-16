"""Granos de arena en la playa de la Concha y longitud de playas hipotéticas.

Hipótesis:
  - La Concha: 1 km de largo, 300 m de ancho, 1 m de arena seca hasta el agua.
  - Grano de arena: esfera de diámetro d (arena fina, 0,2-0,5 mm).
  - Empaquetamiento aleatorio de esferas: ~60 % del volumen es arena.

Uso: python3 scripts/concha.py
"""
import math

LARGO, ANCHO, PROFUNDO = 1000.0, 300.0, 1.0   # m
EMPAQUETAMIENTO = 0.6
DIAMETROS_MM = [0.2, 0.3, 0.5]

UA = 1.496e11        # m
ANYO_LUZ = 9.461e15  # m


def granos_por_m3(d_mm):
    d = d_mm * 1e-3
    v_grano = math.pi / 6 * d**3
    return EMPAQUETAMIENTO / v_grano


def longitud(n_granos, d_mm):
    """Longitud (m) de una playa con la sección de la Concha y n_granos."""
    seccion = ANCHO * PROFUNDO
    return n_granos / (granos_por_m3(d_mm) * seccion)


def fmt_long(m):
    km = m / 1e3
    s = f"{km:.3g} km"
    if m > 0.05 * UA:
        s += f" = {m / UA:.3g} UA"
    if m > 0.01 * ANYO_LUZ:
        s += f" = {m / ANYO_LUZ:.3g} años luz"
    return s


if __name__ == "__main__":
    vol = LARGO * ANCHO * PROFUNDO
    print(f"Volumen de arena de la Concha: {vol:.3g} m^3\n")
    for d in DIAMETROS_MM:
        n = granos_por_m3(d) * vol
        print(f"Grano de {d} mm:")
        print(f"  granos en la Concha: {n:.3g}")
        for N in (1e17, 1e20, 1e27):
            print(f"  playa con {N:.0e} granos: {fmt_long(longitud(N, d))}")
        print()
