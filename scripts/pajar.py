"""¿Cuán grande es el pajar que esconde la aguja?

Fondo/señal de un experimento de doble beta sin blindar (ver
fondo_caverna.py): ~2e12 gammas peligrosos al año frente a ~0,2 sucesos
de señal al año -> un pajar de 1e13 briznas por cada aguja.

Hipótesis:
  - Brizna de paja: cilindro de 30 cm de largo y 3 mm de diámetro.
  - En un pajar suelto la paja ocupa ~10 % del volumen.
  - Densidad del pajar ~60 kg/m3.

Uso: python3 scripts/pajar.py
"""
import math

FONDO = 2e12      # gammas peligrosos por año sobre el detector
SENAL = 0.2       # sucesos de señal por año
N = FONDO / SENAL

L_BRIZNA, D_BRIZNA = 0.30, 3e-3   # m
FRACCION_PAJA = 0.10
RHO_PAJAR = 60.0                  # kg/m3

CAMPO_FUTBOL = 105 * 68           # m2
DONOSTIA = 61e6                   # m2
GIPUZKOA = 1980e6                 # m2
PAJA_POR_HA = 4.0                 # toneladas de paja por hectárea de trigo

if __name__ == "__main__":
    v_brizna = math.pi * (D_BRIZNA / 2)**2 * L_BRIZNA
    V = N * v_brizna / FRACCION_PAJA
    masa_t = V * RHO_PAJAR / 1e3

    print(f"Fondo/señal: {FONDO:.0e} / {SENAL} = {N:.0e} briznas por aguja\n")
    print(f"Volumen del pajar: {V:.2e} m3")
    print(f"Masa:              {masa_t:.2e} toneladas")
    print(f"Cubo de lado:      {V**(1/3):.0f} m")
    print(f"Sobre un campo de fútbol: {V/CAMPO_FUTBOL/1e3:.0f} km de altura")
    print(f"Sobre Donostia:           {V/DONOSTIA:.1f} m de paja")
    print(f"Sobre Gipuzkoa:           {V/GIPUZKOA*100:.0f} cm de paja")
    print(f"Tierra de trigo necesaria: {masa_t/PAJA_POR_HA/100:.0f} km2")
