# PFK2026 — Charla para Passion for Knowledge (Donostia, 2026)

## Objetivo del proyecto

Preparar una charla de **media hora** para el festival **Passion for Knowledge**
(Donostia / San Sebastián, 2026).

- **Audiencia:** gran público. Divulgación, sin formalismo ni ecuaciones innecesarias.
- **Idioma:** español (texto de las transparencias y notas del orador).
- **Herramienta:** LaTeX + Beamer, al menos para el borrador de las transparencias.
- **Autor:** J.J. Gómez Cadenas (DIPC).

## Plan

El plan de trabajo (estructura de la charla, guion, lista de figuras, calendario)
está en [Plan.md](Plan.md). Consultarlo y mantenerlo actualizado antes de tocar
las transparencias.

## Material de referencia

- Lecciones anteriores sobre neutrinos en Beamer: `../LecturesFH/nuFHL1.tex`
  (y siguientes). Sirven de cantera de figuras, macros y estilo Beamer
  (tema Boadilla, 16:9, color `uwopurple`), pero su nivel es de curso
  universitario y su texto está en inglés; hay que adaptar, no copiar.

## Estructura y compilación

- `unicornios.tex`: transparencias. Una por latido de `Plan.md`. Las figuras
  que faltan aparecen como cajas moradas (`\pendiente{...}`).
- `figs/fh/`: copias de `../LecturesFH`; `figs/dp2018/`: copias de
  `../donostiphys2018/img`; `figs/petalo/`: extraídas de `PetaloConcepts.pdf`.
  Los dos primeros directorios están separados porque hay nombres que solo
  difieren en mayúsculas y el sistema de ficheros no las distingue.
- Compilar: `pdflatex unicornios.tex` (dos pasadas). No dejar `.aux`, `.nav`,
  `.snm`, `.log` en el repositorio.
