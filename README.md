# Irrigation — open-source engineering resources

Raccolta di repository open source per lo studio, la didattica e l'analisi tecnica dell'irrigazione agricola: reti in pressione, aspersione, progettazione delle pompe, irrigazione superficiale, bilancio idrico e irrigazione di precisione.

> **Tipo di collegamento:** catalogo di riferimenti GitHub, senza importare codice né installare automaticamente dipendenze. I progetti restano autonomi e mantengono le proprie licenze.

## Repository collegati

**Totale: 24 repository pubblici** (10 della selezione iniziale + 14 nuove aggiunte).

### Progettazione idraulica e irrigazione ad aspersione

| Software | Repository | Ambito di interesse |
| --- | --- | --- |
| **OpenIrri** | [El-Naggar8876/openirri](https://github.com/El-Naggar8876/openirri) | Progettazione di impianti ad aspersione fissi (*solid-set*): irrigatori, condotte, Hazen–Williams, fattore F di Christiansen, pompe e costi. |
| **Sprinkler Distribution Evaluator** | [m-behery/sprinkler-distribution-evaluator](https://github.com/m-behery/sprinkler-distribution-evaluator) | Distribuzione pluviometrica, sovrapposizione degli irrigatori e uniformità su schemi rettangolari o triangolari. |
| **OpenCADIrrigation** | [videjunior/opencadirrigation](https://github.com/videjunior/opencadirrigation) | Disegno e dimensionamento di reti irrigue in pressione, zone e condotte; esportazione di documentazione tecnica. |

### Reti idrauliche e ottimizzazione

| Software | Repository | Ambito di interesse |
| --- | --- | --- |
| **EPANET (OpenWaterAnalytics)** | [OpenWaterAnalytics/EPANET](https://github.com/OpenWaterAnalytics/EPANET) | Simulazione idraulica delle reti in pressione: perdite di carico, pressioni, portate, pompe e valvole. |
| **Pipe Network Optimiser** | [HimanshuKhanve/pipe-network-optimiser](https://github.com/HimanshuKhanve/pipe-network-optimiser) | Ottimizzazione dei diametri e dei costi delle reti, integrazione con modelli EPANET e QGIS. |

### Pompe ed energia

| Software | Repository | Ambito di interesse |
| --- | --- | --- |
| **pvpumpingsystem** | [tylunel/pvpumpingsystem](https://github.com/tylunel/pvpumpingsystem) | Modellazione di sistemi di pompaggio idrico alimentati da energia fotovoltaica. |

### Fabbisogni idrici e irrigazione di precisione

| Software | Repository | Ambito di interesse |
| --- | --- | --- |
| **AquaCrop-OSPy** | [aquacropos/aquacrop](https://github.com/aquacropos/aquacrop) | Simulazione suolo–acqua–coltura e risposta produttiva agli apporti irrigui. |
| **pyfao56** | [kthorp/pyfao56](https://github.com/kthorp/pyfao56) | Approccio FAO-56 del coefficiente colturale duale, bilancio idrico e programmazione irrigua. |
| **PI-Advisor** | [wateraccounting/PI-Advisor](https://github.com/wateraccounting/PI-Advisor) | Supporto alle decisioni nell'irrigazione di precisione, FAO-56 e dati geospaziali. |

### Irrigazione superficiale

| Software | Repository | Ambito di interesse |
| --- | --- | --- |
| **SURCOS** | [jburguete/surcos](https://github.com/jburguete/surcos) | Simulazione dell'irrigazione e fertirrigazione nei solchi, singoli o in rete. |


## Nuovi repository aggiunti (20 novembre 2026)

Questi **14 progetti** si aggiungono ai **10 repository** elencati sopra, per un totale di **24 riferimenti GitHub**. I collegamenti non importano codice né installano software.

### Progettazione idraulica e GIS

*Modelli idraulici e progettazione su cartografia*

| Software | Repository | Applicazione e limiti |
| --- | --- | --- |
| **Irrigation Designer Spatial** | [Narayan1985/Irrigation-Designer](https://github.com/Narayan1985/Irrigation-Designer) | Plugin QGIS per la progettazione preliminare di reti irrigue, aspersione/goccia, quote DEM, pressione, perdite di carico e pompe. |
| **DripIrrigationHydraulics** | [ZWXYM/DripIrrigationHydraulics](https://github.com/ZWXYM/DripIrrigationHydraulics) | Calcoli e ottimizzazione delle reti a goccia in Python; contiene moduli GA/PSO, ma documentazione limitata. |
| **hydirrig** | [joaobtj/hydirrig](https://github.com/joaobtj/hydirrig) | Pacchetto R per calcoli di progettazione idraulica irrigua; aggiornamenti meno recenti. |
| **WNTR** | [USEPA/WNTR](https://github.com/USEPA/WNTR) | Libreria Python compatibile con EPANET per reti in pressione, domande dipendenti dalla pressione, simulazione e analisi. |
| **EngCalcs** | [hawstom/engcalcs](https://github.com/hawstom/engcalcs) | Raccolta di calcolatori idraulici; verificare i moduli specifici prima di usarli in un contesto didattico. |

### Pivot e rotoloni

*Macchine irrigue e rateo variabile*

| Software | Repository | Applicazione e limiti |
| --- | --- | --- |
| **VRI Pivô** | [romariocarvalhoneto/vri_pivo](https://github.com/romariocarvalhoneto/vri_pivo) | Plugin QGIS per zone di gestione e irrigazione a rateo variabile dei pivot; settori radiali e controllo della velocità. |
| **Irrigation Reel Controller** | [Reed1717/Irrigation-Reel-Controller](https://github.com/Reed1717/Irrigation-Reel-Controller) | Prototipo per il controllo della velocità dei rotoloni irrigui; repository piccolo e non recentemente aggiornato. |

### Evapotraspirazione e pianificazione

*ET₀, telerilevamento e programmazione irrigua*

| Software | Repository | Applicazione e limiti |
| --- | --- | --- |
| **pyet** | [pyet-org/pyet](https://github.com/pyet-org/pyet) | Libreria Python per evapotraspirazione potenziale e di riferimento, inclusi metodi FAO-56, ASCE-PM e altri. |
| **OpenET Reference ET** | [Open-ET/openet-refet-gee](https://github.com/Open-ET/openet-refet-gee) | Funzioni di evapotraspirazione di riferimento standardizzata ASCE in Google Earth Engine. |
| **OpenET geeSEBAL** | [Open-ET/openet-geesebal](https://github.com/Open-ET/openet-geesebal) | Modello di evapotraspirazione effettiva basato su bilancio energetico e dati satellitari Landsat. |
| **IrrigationScheduler** | [GreenSmart-DSS/IrrigationScheduler](https://github.com/GreenSmart-DSS/IrrigationScheduler) | Framework Python per il bilancio idrico dello strato radicale e la programmazione irrigua. |
| **Exact Hydraulic Caching** | [Iqx-nwafu/Exact-hydraulic-caching-for-event-driven-rotational-irrigation-scheduling-under-stochastic-failures](https://github.com/Iqx-nwafu/Exact-hydraulic-caching-for-event-driven-rotational-irrigation-scheduling-under-stochastic-failures) | Esperimenti riproducibili su turnazione irrigua, guasti e verifiche idrauliche con EPANET/WNTR. |

### Controllo automatico

*Automazione e supervisione degli impianti*

| Software | Repository | Applicazione e limiti |
| --- | --- | --- |
| **SIP** | [Dan-in-CA/SIP](https://github.com/Dan-in-CA/SIP) | Software Raspberry Pi per controllo irriguo, elettrovalvole e calendari di irrigazione. |
| **OSPy** | [martinpihrt/OSPy](https://github.com/martinpihrt/OSPy) | Controllore irriguo estensibile basato su Raspberry Pi, timer e plugin. |

### Nota sulla qualità delle fonti

I repository hanno livelli di maturità diversi: alcuni sono strumenti scientifici documentati, altri prototipi o sperimentazioni. Prima di integrare algoritmi nei materiali didattici occorre confrontare formule, ipotesi, casi di test e licenze. L'inclusione nel catalogo non rappresenta una validazione indipendente.

## Percorsi di studio e confronto

1. **Aspersione e uniformità:** confrontare OpenIrri con Sprinkler Distribution Evaluator; distinguere le stime semplificate di uniformità dalle distribuzioni misurate/simulate.
2. **Reti in pressione:** confrontare i risultati di OpenIrri o OpenCADIrrigation con EPANET; verificare portate, perdite di carico, pressioni al nodo critico e diametri.
3. **Ottimizzazione economica:** utilizzare Pipe Network Optimiser per studiare il compromesso fra diametro, investimento iniziale e vincoli idraulici.
4. **Stazioni di pompaggio:** analizzare la curva caratteristica della pompa, la curva dell'impianto, il rendimento, l'NPSH e gli eventuali sistemi fotovoltaici.
5. **Gestione dell'irrigazione:** confrontare FAO-56/pyfao56, AquaCrop-OSPy e PI-Advisor per stimare fabbisogni e turni irrigui.
6. **Irrigazione superficiale:** utilizzare SURCOS per studi sul moto dell'acqua nei solchi.

## Precauzioni scientifiche

- La disponibilità del codice sorgente **non dimostra di per sé** la validazione idraulica o agronomica.
- Controllare sempre le ipotesi di progetto, le unità di misura, le condizioni al contorno, i valori dei parametri e i limiti dei modelli.
- Le licenze differiscono tra i progetti: il semplice link non comporta incorporazione del codice; prima di riutilizzarlo verificare licenze e obblighi di attribuzione.
- I progetti esterni cambiano nel tempo; per risultati riproducibili registrare tag, commit o release utilizzati.

## Stato del collegamento

I link sopra rimandano ai repository originali e sono stati verificati come accessibili il **20 novembre 2026**.

Questo repository è attualmente un **hub di documentazione e collegamenti**. Non contiene ancora submodule Git, fork o una pipeline software che esegua automaticamente i progetti elencati.
