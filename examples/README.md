# Esercitazione: OpenIrri, calcolo analitico ed EPANET

**Ambito:** impianto ad aspersione fisso (solid-set), una condotta principale, una sottoprincipale e quattro ali.

## Dati di progetto

| Parametro | Valore |
| --- | ---: |
| Ali irrigue | 4 |
| Erogatori per ala | 32 |
| Portata per erogatore | 0,52 m3/h |
| Portata totale | 66,56 m3/h |
| Interasse irrigatori | 12,6 m |
| Lunghezza ala | 403,2 m |
| Diametro interno condotta principale | 176 mm |
| Lunghezza condotta principale | 270 m |
| Diametro interno sottoprincipale | 110 mm |
| Lunghezza sottoprincipale | 4 x 30 m |
| Coefficiente Hazen-Williams | C = 150 |
| Diametri interni ali confrontati | 55,4 mm e 66,0 mm |
| Pressione minima richiesta | 28 m c.a. |
| Quote delle ali | 7, 8, 9, 10 m |

Curva sintetica della pompa: H(Q) = 61 - 0,0025 Q^2, con H in m e Q in m3/h; non rappresenta un costruttore.

## Metodo di confronto

- Calcolare le perdite di carico con Hazen-Williams (exponenti 1,852 e 4,87).
- Calcolare le perdite delle ali con il fattore F di Christiansen.
- Ripetere il calcolo sommando le perdite di ciascuno dei 32 tratti con portata progressivamente decrescente.
- Ricostruire i carichi piezometrici e identificare l'irrigatore piu' sfavorito.
- Per una verifica indipendente, modellare la rete in EPANET 2.2 e confrontare risultati, ipotesi e unita'.

## Risultati analitici e dalle formule OpenIrri

| Grandezza | Diametro 55,4 mm | Diametro 66,0 mm |
| --- | ---: | ---: |
| Perdita principale (m) | 0,784 | 0,784 |
| Perdita sottoprincipale (m) | 1,667 | 1,667 |
| Perdita ala, somma 32 tratti (m) | 9,161 | 3,905 |
| Perdita ala, fattore F (m) | 9,161 | 3,905 |
| Prevalenza minima richiesta (m) | 49,611 | 44,356 |
| Prevalenza pompa a Q = 66,56 m3/h (m) | 49,924 | 49,924 |
| Pressione all'ultimo irrigatore sfavorito (m) | 28,313 | 33,569 |

## Avvertenze

Questa scheda riporta risultati analitici di un caso sintetico elaborato il 20 novembre 2026. **Non e' un report ottenuto dal solver EPANET**: il modello EPANET era stato predisposto, ma non eseguito. Inoltre le portate dei singoli irrigatori sono qui assunte indipendenti dalla pressione (DDA), e le perdite localizzate sono nulle.

Codice di riferimento OpenIrri: https://github.com/El-Naggar8876/openirri

Manuale e toolkit EPANET: https://github.com/OpenWaterAnalytics/EPANET

[Vai al catalogo](../docs/CATALOGO_COMPLETO.md)
