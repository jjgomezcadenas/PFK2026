# Plan de la charla — Passion for Knowledge, Donostia 2026

**Estado:** versión final (2026-09-17). Contenido cerrado; queda el ensayo.
Las versiones anteriores del plan están en `docs/Plan-v2-2026-09-04.md` y en
la historia del repositorio.

## Título

**¿Para qué sirven los unicornios?**

## Duración

40–42 minutos. 44 transparencias, diez de ellas con aparición por pasos
(unos 20 clics en total). Las tres de hardware de NEXT pasan en pocos
segundos cada una.

## Tesis

Un solo unicornio: el neutrino. Pauli lo inventa en 1930 como "remedio
desesperado" para salvar la conservación de la energía. Eddington no cree en
él. Reines y Cowan lo cazan en 1956 jugando a la lotería de Babilonia:
probabilidad ínfima por número gigantesco. Hoy vemos neutrinos del reactor,
del Sol y de los confines de la galaxia; vigilan la proliferación nuclear, y
Eddington tendría que creer. Y el unicornio puede ser la respuesta a por qué
existe el Universo: si es su propia antipartícula (Majorana), sus antepasados
pesados inclinaron la balanza hacia la materia. NEXT busca la prueba en
Canfranc: una desintegración por tonelada y año, escondida en un pajar que
cubre Donostia hasta los tejados. Cierre: la sublime utilidad de la ciencia
inútil (Echenique, Deutsch) y Rilke.

## Marco narrativo

- **Rilke**, *Sonetos a Orfeo* II.4, con el cuadro de Arthur B. Davies.
  Primera estrofa al abrir, segunda al cerrar, traducción JJGC.
- **El fantasma**: el neutrino se dibuja como fantasma desde que Pauli lo
  propone (atraviesa el plomo, choca en Poltergeist, se escapa del reactor,
  engorda hasta sumo como neutrino pesado, se funde consigo mismo en la doble
  beta sin neutrinos).
- **La lotería de Babilonia** (Borges): probabilidad mínima por número
  enorme. Se usa dos veces: para cazar el neutrino en el reactor y para
  esperar una doble beta sin neutrinos en una tonelada de xenón.
- **La playa**: los granos de arena de las playas de Donostia como unidad
  de número grande. La Concha, Ondarreta y Zurriola tienen 10^17 granos; el
  reactor produce una playa hasta Pekín cada segundo; la playa de Babilonia
  (10^28 granos) llega a 3000 veces la distancia al Sol. Cálculos en
  `scripts/concha.py`.
- **Código visual** de las figuras generadas: núcleo = racimo de bolas rojas
  y grises, electrón = bola azul, neutrino = fantasma (o bola verde en la
  desintegración beta), positrón = bola roja.

## Estructura (44 transparencias)

| Bloque | Transp. | Min |
|---|---|---|
| 0. Teaser: Rilke | 1–2 | 2 |
| 1. Nace el unicornio: Becquerel, beta, balanza, histogramas, Pauli, Eddington | 3–13 | 11 |
| 2. Cazar al unicornio: lotería, playa, Poltergeist, Vandellós, proliferación, Sol, IceCube, Sir Arthur | 14–24 | 11 |
| 3. ¿Sirven para algo? (lista, "crear universos" en rojo) | 25 | 1 |
| 4. Antimateria y origen del Universo: Majorana, agente doble, naufragio, fórmula | 26–32 | 6 |
| 5. Doble o nada: doble beta, ángel y montaña, Babilonia revisitada, pajar, NEXT | 33–41 | 7 |
| 6. Cierre: Ítaca, ciencia básica, Rilke | 42–44 | 3 |

## Guion

1. Portada (azul).
2. **Unicornios.** Davies y Rilke, primera estrofa.
3. **Radiactividad.** Placa de Becquerel, 1896.
4. **Desintegración beta.** Núcleo → núcleo + electrón (imagen generada).
5. **La energía del electrón.** Balanza en equilibrio: tritio = helio-3 +
   electrón. *3 pasos.*
6. **La energía debería ser siempre la misma.** Histograma TikZ: 1, 2,
   muchas entradas en la misma columna. *3 pasos.*
7. **Pero cada electrón tenía una energía diferente.** Mismo esquema,
   espectro continuo 1-5-10-15-10-5-3-2-1. *3 pasos.*
8. **Conservación de la energía.** ¿Dónde se iba la energía? Anathema sit.
9. **Un remedio desesperado.** Carta de Pauli.
10. **¿Por qué desesperado?** Las leyes son las mismas aquí y en Andrómeda.
11. **¿Cuál era el remedio?** Segunda partícula (bola verde) y la balanza.
12. **Fantasmas y unicornios.** Cuatro años luz de plomo hasta Alfa
    Centauri; los fantasmas atraviesan la pared.
13. **La gente seria no cree en los unicornios.** Eddington, 1935.
14. **La lotería de Babilonia.** Borges.
15. **Contando granos de arena.** Las playas de Donostia: 10^17 granos, en
    recuadro al clic. *2 pasos.*
16. **Una playa entre Donosti y Pekín.** 2 × 10^20 neutrinos por segundo.
17. **Proyecto Poltergeist.** Reines y Cowan; el fantasma choca con el
    neutrón. *2 pasos.*
18. **Setenta años más tarde en Vandellós.** Detector de sobremesa.
19. **El fantasma y la proliferación nuclear.** Reactor, ladrón de
    plutonio, detector cazafantasmas. Responde a Eddington: "aplicaciones".
20. **Neutrinos solares.** Super-Kamiokande, neutrinografía del Sol.
21. **Paisaje con neutrinos.** Comanches / IceCube.
22. **IceCube.** Un kilómetro cúbico de hielo.
23. **Neutrinos galácticos.** Aceleradores cósmicos.
24. **Sir Arthur, quizás tendrás que creer.** Todas las fuentes en 2026.
25. **¿Sirven para algo los neutrinos?** Lista: la Tierra, ¡y el Sol!, ¡y la
    galaxia!, ¡y los agujeros negros!, y en rojo "Para crear universos".
    *5 pasos.*
26. **Antimateria.** Positrón de Anderson.
27. **La materia y la antimateria se aniquilan.**
28. **¿Por qué existe el Universo?** Mini Big Bang del LHC.
29. **El neutrino de Majorana.** Sin carga, puede ser su propia
    antipartícula (1937).
30. **Un agente doble.** Sumo que escupe un electrón; su espejo, un
    positrón. *3 pasos.*
31. **Nuestro Universo son los restos de un naufragio.**
32. **La fórmula del Universo.** Escher + farola + Hubble.
33. **Doble o nada.** Jinetes de Escher; casino subterráneo.
34. **Desintegración doble beta sin neutrinos.** Con fantasmas / los
    fantasmas se funden.
35. **El ángel y la montaña.** Cada segundo del Universo alargado a la vida
    del Universo: 10^27–10^28 años. Playa de Babilonia.
36. **Babilonia revisitada.** Una tonelada de xenón, tantas papeletas como
    granos, tantos sorteos como granos: una desintegración al año. *3 pasos.*
37. **La Tierra es un planeta muy radioactivo.** 4 g de uranio y 15 g de
    torio por tonelada; billones de fotones; el pajar cubre Donostia hasta
    los tejados. Cálculos en `scripts/fondo_caverna.py` y `scripts/pajar.py`.
    *3 pasos: texto, hombre en el pajar, Donostia bajo paja.*
38. **NEXT.** Detector futurista; la balanza del xenón al clic. *2 pasos.*
39. **Vasija a presión y blindaje de cobre.** (rápida)
40. **Plano de energía y plano de trazas.** (rápida)
41. **Jaula de campo y tubo de luz.** (rápida)
42. **El camino a Ítaca.** Berkeley 2009; viajes de veinte años; Cavafis.
43. **¿Para qué sirven los unicornios?** Viñeta de Forges; Echenique, la
    sublime utilidad de la ciencia inútil; Deutsch, Atenas y Esparta.
44. **El unicornio.** Rilke, segunda estrofa; imagen; Eskerrik asko.

## Decisiones tomadas

- Un solo unicornio, el neutrino. La antimateria solo como ingrediente del
  origen del Universo.
- La proliferación nuclear se queda como única aplicación: responde a
  Eddington, que pidió "aplicaciones industriales".
- Los números de la cadena playa–Babilonia–xenón son consistentes en orden
  de magnitud; no se afina más para el gran público.
- La cita de Deutsch es una paráfrasis, asumida. Grafía "Etxenique" tal
  como está.
- Las tres figuras con rótulos en inglés (Antimateria, IceCube, fuentes de
  neutrinos) se dejan como están.
- Las transparencias de NEXT van una a una, un mensaje cada vez.
- Animaciones con `\visible`, solo donde la aparición por pasos es el
  argumento (diez transparencias).
- Formato: paleta y tipografía de la propuesta de Claude Design
  (`uniDesign.pdf`): fondo crema, azul de acento, IBM Plex Sans y Playfair
  Display, portada azul, sin pie de página, 10 pt.

## Producción

- `unicornios.tex`, Beamer 16:9, tema default personalizado. Compilar con
  `pdflatex`, dos pasadas. 63 páginas, 18 MB.
- Figuras en `figs/` (JPEG de 1920 px las pesadas; los PNG originales en
  `figs/orig/`, fuera del repositorio). `figs/fh/` y `figs/dp2018/` son las
  canteras antiguas.
- Macros TikZ en el preámbulo: histogramas (`\fila`, `\filae`), fantasma,
  núcleo y electrón.
- `scripts/`: estimaciones de granos de arena, fondo radiactivo de la
  caverna y tamaño del pajar.
- Repositorio: `github.com:jjgomezcadenas/PFK2026`, rama `main`.
- No dejar `.aux`, `.log`, `.nav`, `.snm`, `.toc`, `.synctex.gz` en el
  directorio; el PDF no se versiona.
