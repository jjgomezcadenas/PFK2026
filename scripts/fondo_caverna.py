"""Fondo radiactivo (U y Th de la roca) sobre un detector de doble beta sin blindaje.

Geometría:
  - Caverna cilíndrica en granito: 9 m de diámetro, 9 m de largo.
  - Detector cilíndrico en el centro: 3 m de diámetro, 3 m de alto.
  - Roca infinita alrededor (semiespacio en cada pared).

Física (orden de magnitud):
  - Granito típico: U-238 ~50 Bq/kg (~4 ppm), Th-232 ~60 Bq/kg (~15 ppm),
    cadenas en equilibrio secular. Densidad 2650 kg/m3.
  - Los gammas que salen de la roca vienen de una capa de espesor ~1/mu.
    Corriente de gammas no dispersados que sale de un semiespacio con
    fuente uniforme S (gammas/m3/s):  J = S / (4 mu)   [gammas/m2/s].
  - Dentro de la caverna el campo es ~isótropo; el ritmo con que los
    gammas alcanzan un cuerpo convexo de área A es J * A.
  - Líneas peligrosas para la señal (Q_bb del Xe-136 = 2458 keV):
      Bi-214 2448 keV: 1,55 % por desintegración de U-238.
      Tl-208 2615 keV: 35,9 % (rama) x 99,8 % = 0,358 por desint. de Th-232.
  - Gammas totales por desintegración de la cadena (E > ~100 keV): U ~2,2, Th ~2,6.
  - Atenuación en granito: mu ~ 10 /m a 2,5 MeV; ~15 /m para el espectro medio.

Uso: python3 scripts/fondo_caverna.py
"""
import math

# --- geometría (m) ---
D_CAV, L_CAV = 9.0, 9.0
D_DET, H_DET = 3.0, 3.0

# --- roca ---
RHO = 2650.0            # kg/m3
A_U, A_TH = 50.0, 60.0  # Bq/kg
MU_HI, MU_MED = 10.0, 15.0   # 1/m

# --- gammas por desintegración ---
Y_U_2448, Y_TH_2615 = 0.0155, 0.358
Y_U_TOT, Y_TH_TOT = 2.2, 2.6

# --- señal de referencia ---
M_XE, T_HALF = 1000.0, 1e28    # kg de Xe-136, años
SEG_ANYO = 3.156e7


def area_cilindro(d, h):
    r = d / 2
    return 2 * math.pi * r * h + 2 * math.pi * r**2


def corriente(S, mu):
    """Gammas/m2/s que salen de la roca hacia la caverna."""
    return S / (4 * mu)


if __name__ == "__main__":
    A_cav = area_cilindro(D_CAV, L_CAV)
    A_det = area_cilindro(D_DET, H_DET)
    print(f"Área de las paredes de la caverna: {A_cav:.0f} m2")
    print(f"Área del detector:                 {A_det:.1f} m2")
    print(f"Fracción geométrica que alcanza el detector: {A_det/A_cav:.2f}\n")

    capa = 1 / MU_MED
    m_roca = A_cav * capa * RHO
    print(f"Capa de roca que 've' el detector: ~{capa*100:.0f} cm, {m_roca/1e3:.0f} toneladas")
    print(f"Actividad U+Th de esa capa: {m_roca*(A_U+A_TH):.2e} Bq\n")

    # todos los gammas
    S_tot = RHO * (A_U * Y_U_TOT + A_TH * Y_TH_TOT)
    J_tot = corriente(S_tot, MU_MED)
    print("GAMMAS DE TODAS LAS ENERGÍAS")
    print(f"  salen de las paredes:    {J_tot*A_cav:.2e} /s")
    print(f"  alcanzan el detector:    {J_tot*A_det:.2e} /s  = {J_tot*A_det*SEG_ANYO:.1e} /año\n")

    # líneas cerca de Q_bb
    S_2448 = RHO * A_U * Y_U_2448
    S_2615 = RHO * A_TH * Y_TH_2615
    r_2448 = corriente(S_2448, MU_HI) * A_det
    r_2615 = corriente(S_2615, MU_HI) * A_det
    print("GAMMAS CERCA DE Q_bb (2458 keV) QUE ALCANZAN EL DETECTOR")
    print(f"  Bi-214 2448 keV (uranio): {r_2448:.2e} /s")
    print(f"  Tl-208 2615 keV (torio):  {r_2615:.2e} /s")
    print(f"  total:                    {r_2448+r_2615:.2e} /s  = {(r_2448+r_2615)*SEG_ANYO:.1e} /año\n")

    # señal
    N = M_XE * 1e3 / 136 * 6.022e23
    senal = N * math.log(2) / T_HALF
    print(f"SEÑAL: {M_XE:.0f} kg de Xe-136, T1/2 = {T_HALF:.0e} años -> {senal:.2f} sucesos/año")
    print(f"Fondo potencial (líneas cerca de Q_bb) / señal: {(r_2448+r_2615)*SEG_ANYO/senal:.1e}")
