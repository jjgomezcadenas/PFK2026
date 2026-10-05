# Plan de la charla — Passion for Knowledge, Donostia 2026

**Estado:** versión final revisada (2026-10-05). Contenido cerrado; queda el
ensayo. Las versiones anteriores del plan están en
`docs/Plan-v2-2026-09-04.md` y en la historia del repositorio (la del
2026-09-17 en el commit `21004cf`).

## Título

**¿Para qué sirven los unicornios?**

## Duración

45 minutos. 52 transparencias (77 páginas contando la aparición por pasos).
Las tres de hardware de NEXT pasan en pocos segundos cada una.

## Tesis

Un solo unicornio: el neutrino. Pauli lo inventa en 1930 como "remedio
desesperado" para salvar la conservación de la energía. Eddington no cree en
él, salvo que alguien lo fabrique y le encuentre aplicaciones. Reines y Cowan
lo cazan en 1956 junto a un reactor; hoy vemos neutrinos del reactor, del Sol
y de los confines de la galaxia, y Eddington tendría que creer. Y el unicornio
puede ser la respuesta a por qué existe el Universo: si es su propia
antipartícula (Majorana), sus antepasados pesados inclinaron la balanza hacia
la materia. NEXT busca la prueba en Canfranc: la lotería de lo imposible
(probabilidad absurdamente pequeña por número de átomos absurdamente grande)
da del orden de una desintegración al año en cinco toneladas de xenón,
escondida en un pajar del tamaño de Donostia. BOLD quiere además atrapar el
átomo de bario. Cierre: las aplicaciones que pedía Eddington, de los ladrones
de plutonio al cáncer y al Club Galáctico, terminando en "crear universos", y
Rilke.

## Marco narrativo

- **Rilke**, *Sonetos a Orfeo* II.4, con el cuadro de Arthur B. Davies.
  Primera estrofa al abrir; al cerrar, el soneto hasta "podría llegar a ser".
  Traducción JJGC.
- **Eddington y las aplicaciones**: la cita de 1935 ("si lo consiguen y, quién
  sabe, les encuentran aplicaciones", en azul) se contesta dos veces: "Sir
  Arthur, quizás tendrás que creer" y el bloque final "¿Para qué sirven los
  unicornios?", donde cada transparencia es una respuesta y lleva su propio
  título.
- **La playa**: los granos de arena de las playas de Donostia como unidad
  de número grande. La Concha, Ondarreta y Zurriola tienen 10^17 granos; el
  reactor produce una playa hasta Pekín cada segundo. Cálculos en
  `scripts/concha.py`.
- **El ruiseñor y la montaña** (10^28 años) y **la lotería de lo imposible**
  (5 toneladas de xenón ~ 10^28 átomos): casi cero por casi infinito, del
  orden de uno.
- **Código visual**: las figuras generadas siguen un estilo de gouache sobre
  papel, sin efectos "de IA". El neutrino es un unicornio fantasmal de tapiz
  medieval (atraviesa el plomo, choca con el protón en Poltergeist, huye del
  reactor del ladrón); el neutrino pesado N es un unicornio de tiro
  (percherón); en la doble beta sin neutrinos los dos unicornios cruzan los
  cuernos y se disuelven. Electrón azul en el agente doble; en Poltergeist la
  bola azul es el positrón y la roja el neutrón (no se ha unificado).

## Estructura (52 transparencias)

| Bloque | Transp. | Min |
|---|---|---|
| 0. Teaser: Rilke | 1–2 | 2 |
| 1. Nace el unicornio: Becquerel, beta, balanza, histogramas, Vasari, Pauli, Eddington | 3–13 | 11 |
| 2. Cazar al unicornio: playa, Pekín, Poltergeist, Vandellós, Sol, IceCube, Sir Arthur | 14–22 | 8 |
| 3. Antimateria y origen del Universo: Majorana, agente doble, naufragio | 23–28 | 6 |
| 4. Doble o nada: doble beta, xenón, ruiseñor, lotería de lo imposible, pajar | 29–37 | 8 |
| 5. NEXT y BOLD | 38–44 | 5 |
| 6. ¿Para qué sirven los unicornios? Aplicaciones | 45–51 | 4 |
| 7. Cierre: Rilke | 52 | 1 |

## Guion

1. Portada (azul).
2. **Unicornios.** Davies y Rilke, primera estrofa, a la vez.
3. **Radiactividad.** Placa de Becquerel, 1896. *3 pasos: imagen,
   Becquerel, los Curie.*
4. **Desintegración beta.** Núcleo → núcleo + electrón.
5. **La energía del electrón.** Balanza: tritio = helio-3 + electrón. *3
   pasos.*
6. **La energía del electrón debería ser siempre la misma.** Histograma
   TikZ. *3 pasos.*
7. **Pero cada electrón tenía una energía diferente.** Espectro continuo.
   *3 pasos.*
8. **Conservación de la energía.** Fresco de Vasari (Gregorio IX excomulga
   a Federico II); ¿dónde se iba la energía? Anathema sit.
9. **Un remedio desesperado.** Carta de Pauli a los participantes del
   congreso de Tübingen.
10. **¿Por qué desesperado?** Energía y leyes que no cambian con el
    tiempo.
11. **¿Cuál era el remedio? Desnudar a un santo para vestir a otro.**
    Segunda partícula y la balanza.
12. **Unicornios fantasmales.** Cuatro años luz de plomo hasta Alfa
    Centauri; los unicornios recorren la barra de plomo por dentro.
13. **La gente seria no cree en los unicornios.** Eddington, 1935.
14. **Contando granos de arena.** 10^17 granos, en recuadro al clic. *2
    pasos.*
15. **Una playa entre Donosti y Pekín.** 2 × 10^20 neutrinos por segundo.
16. **Proyecto Poltergeist.** Equipo de 1953 y el unicornio que golpea el
    protón; (anti) electrones y (anti) neutrinos.
17. **Setenta años más tarde en Vandellós.** Detector de sobremesa.
18. **Neutrinos solares.** Diagrama pp (dominio público).
19. **Cómo detectamos neutrinos solares.** Super-Kamiokande,
    neutrinografía.
20. **Paisaje con neutrinos.** Comanches / IceCube.
21. **IceCube.**
22. **Sir Arthur, quizás tendrás que creer.** Todas las fuentes en 2026.
23. **Antimateria.** Positrón de Anderson.
24. **En el cosmos no hay (casi) antimateria.** *3 pasos.*
25. **El Universo no debería existir.** Mini Big Bang del LHC. *3 pasos.*
26. **El neutrino de Majorana.** e± y manos de Escher; Majorana según
    Fermi (texto comentado, se cuenta de palabra).
27. **Un agente doble.** Unicornio pesado que emite un electrón; su
    espejo, un positrón. *3 pasos.*
28. **Nuestro Universo son los restos de un naufragio.**
29. **Doble o nada.** Jinetes de Escher; casino subterráneo.
30. **Desintegración doble beta sin neutrinos.** Unicornios que escapan /
    unicornios que se aniquilan. *2 pasos.*
31. **El gas noble de (luz) azul.** Xenón, tubo de descarga, faros de
    coche.
32. **El xenón se desintegra doble beta.** Xe-136 → Ba-136.
33. **El ruiseñor y la montaña.** El ruiseñor se cuenta con la imagen; el
    genio que alarga cada segundo; recuadro 10^28 años. *3 pasos.*
34. **La lotería de lo imposible.** Papeletas y pregunta; unicornios,
    respuesta y recuadro 5 toneladas ~ 10^28 átomos. *2 pasos.*
35. **La Tierra es un planeta muy radiactivo.** Cadena del uranio; 4 g de
    uranio y 15 g de torio por tonelada; billones de fotones.
36. **Buscar una desintegración doble beta en un pajar.** Solo imagen.
37. **… del tamaño de Donosti.** Solo imagen. Cálculos en
    `scripts/fondo_caverna.py` y `scripts/pajar.py`.
38. **NEXT.** Esquema del detector; la balanza del xenón al clic. *2
    pasos.*
39. **Electrones en NEXT.** Trazas reconstruidas: dos electrones (dos
    «blobs») frente a uno. Sin texto.
40. **BOLD.** Atrapar el bario con una red de moléculas que brillan en
    azul.
41. **And a bit crazy.** Un átomo de Ba entre 10^28 de xenón; Watzlawick.
42. **NEXT está en marcha en el Laboratorio Subterráneo de Canfranc.**
    Invitación a visitarnos. (rápida)
43. **Los «ojos» de NEXT.** Planos de energía y de trazas. (rápida)
44. **La jaula eléctrica para guiar electrones (y el bario).** (rápida)
45. **¿Para qué sirven los unicornios?** Solo el cuadro de Davies.
46. **Para atrapar ladrones de plutonio.** *4 pasos.*
47. **Para (ayudar a) curar el cáncer.** Molécula bicolor, aurkinas y
    curva de volumen tumoral; FPC: The Bold solution.
48. **Para entender mejor la Tierra, el Sol y la galaxia.** Mapa AGM2015,
    corte del Sol, IceCube; una por clic. Es repaso: deprisa. *3 pasos.*
49. **Para comunicaciones privadas (PTP).** Haces de neutrinos on/off.
50. **El Club Galáctico.**
51. **Para crear universos.** Escher + farola + Hubble.
52. **El unicornio.** Rilke hasta "podría llegar a ser"; imagen; Eskerrik
    asko.

Comentadas en el fuente (no salen): La lotería de Babilonia, ¿Para fabricar
los ordenadores cuánticos del futuro?, Comunicaciones interestelares con
neutrinos, El camino a Ítaca, las tres transparencias sueltas de Tierra, Sol y
galaxia (con sus textos) y el texto de la antigua "¿Para qué sirven los
unicornios?" (Echenique, Deutsch).

## Decisiones tomadas

- Un solo unicornio, el neutrino. La antimateria solo como ingrediente del
  origen del Universo.
- Los fantasmas se sustituyen por unicornios en todas las figuras generadas.
- La lotería de Babilonia (Borges) sale de la charla; queda "la lotería de lo
  imposible", sin referencia al relato.
- El bloque final responde a Eddington con aplicaciones concretas, una por
  transparencia; la proliferación nuclear abre el bloque.
- Los números de la cadena playa–ruiseñor–xenón son consistentes en orden de
  magnitud; con 5 toneladas salen del orden de 1–2 desintegraciones al año.
- Figuras con rótulos en inglés (Antimateria, IceCube, cadena del uranio,
  diagrama del xenón, Sol, curva tumoral) se dejan como están.
- Animaciones con `\visible`, solo donde la aparición por pasos es el
  argumento (trece transparencias).
- "Radiactivo" en toda la charla, salvo en la carta de Pauli ("Queridas y
  radioactivas damas y caballeros").
- Formato: paleta y tipografía de la propuesta de Claude Design
  (`uniDesign.pdf`): fondo crema, azul de acento, IBM Plex Sans y Playfair
  Display, portada azul, sin pie de página, 10 pt.

## Pendiente (opcional)

- Poltergeist: la segunda viñeta repite la idea del "(anti)".
- "galaxia" (minúscula) frente a "Galaxia" (Club Galáctico).
- Legibilidad al proyectar: curva tumoral, página del artículo en PTP, carta
  de Pauli.
- Bloque de aplicaciones: es una progresión (mundanas → científicas →
  ciencia ficción → crear universos). Tierra, Sol y galaxia ya van en una
  sola transparencia y las comunicaciones interestelares están comentadas.
  Ritmo: mundanas despacio, científicas deprisa (son repaso), ciencia ficción
  con humor, crear universos como remate.

## Producción

- `unicornios.tex`, Beamer 16:9, tema default personalizado. Compilar con
  `pdflatex`, dos pasadas. 77 páginas, 22 MB.
- Figuras en `figs/`: JPEG para las pesadas (más de 500 KB), originales PNG
  en `figs/orig/`, fuera del repositorio. GIF y WebP se convierten (pdflatex
  no los lee). `figs/fh/` y `figs/dp2018/` son las canteras antiguas.
- Macros TikZ en el preámbulo: histogramas (`\fila`, `\filae`); las de
  fantasma, núcleo y electrón ya no se usan.
- `scripts/`: estimaciones de granos de arena, fondo radiactivo de la
  caverna y tamaño del pajar.
- Repositorio: `github.com:jjgomezcadenas/PFK2026`, rama `main`.
- No dejar `.aux`, `.log`, `.nav`, `.snm`, `.toc`, `.synctex.gz` en el
  directorio; el PDF no se versiona.
