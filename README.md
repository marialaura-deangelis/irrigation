# Irrigation — open-source engineering resources

Raccolta di repository open source per lo studio, la didattica e l'analisi tecnica dell'irrigazione agricola: reti in pressione, aspersione, progettazione delle pompe, irrigazione superficiale, bilancio idrico e irrigazione di precisione.

> **Tipo di collegamento:** catalogo di riferimenti GitHub, senza importare codice né installare automaticamente dipendenze. I progetti restano autonomi e mantengono le proprie licenze.

## Dove trovare il materiale

- [Catalogo dei 61 repository, in file separato](docs/CATALOGO_COMPLETO.md)
- [Schede dei 20 progetti appena aggiunti](docs/NUOVI_20_PROGETTI.md)
- [Guida: collegamenti, codici sorgente e come scaricarli](docs/COME_TROVARE_IL_MATERIALE.md)
- [Studio numerico OpenIrri / EPANET (documentazione)](examples/README.md)
- [Script per scaricare i repository esterni sul proprio computer](scripts/scarica_repositories.py)

## Repository collegati

**Totale: 61 repository pubblici** (10 iniziali + 14 della seconda selezione + 17 della terza selezione + 20 della quarta selezione).

### Progettazione idraulica e irrigazione ad aspersione

| Software | Repository | Ambito di interesse |
| --- | --- | --- |
| **OpenIrri** | [El-Naggar8876/openirri](https://github.com/El-Naggar8876/openirri) | Progettazione di impianti ad aspersione fissi (*solid-set*): irrigatori, condotte, Hazen–Williams, fattore F di Christiansen, pompe e costi. |
| **Sprinkler Distribution Evaluator** | [m-behery/sprinkler-distribution-evaluator](https://github.com/m-behery/sprinkler-distribution-evaluator) | Distribuzione pluviometrica, sovrapposizione degli irrigatori e uniformità su schemi rettangolari o triangolari. |
| **OpenCADIrrigation** | [videjunior/opencadirrigation](https://github.com/videjunior/opencadirrigation) | Disegno e dimensionamento di reti irrigue in pressione, zone e condotte; esportazione di documentazione tecnica. |

**OpenIrri — published references (verified 24 November 2026):**
- Journal article: El-Naggar, A.G. (2026). OpenIrri: An open-source Python platform for solid-set sprinkler irrigation system design. SoftwareX, 35, 102912. https://doi.org/10.1016/j.softx.2026.102912
- Archived software (specific release): El-Naggar, A.G. (2026). OpenIrri — an open-source web application for the design of solid-set sprinkler irrigation systems (v1.0.2) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.20925592
The article and archived release have distinct DOIs. [BibTeX references](docs/references/openirri.bib).

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


## Terza selezione: 17 ulteriori repository (20 novembre 2026)

Modelli di idraulica agraria, idrologia e strumenti collegati alla progettazione e gestione dell'irrigazione. **24 precedenti + 17 nuovi = 41 repository.**

### Idraulica agraria e canali

| Progetto | Repository | Applicazioni e limiti | Tipologia |
| --- | --- | --- | --- |
| **CRITERIA1D / GEO** | [ARPA-SIMC/CRITERIA1D](https://github.com/ARPA-SIMC/CRITERIA1D) | Modello agro-idrologico: flusso nel suolo, fabbisogno irriguo, drenaggio e risalita capillare. | Modello scientifico |
| **Canals** | [darwishdasty-oss/Canals](https://github.com/darwishdasty-oss/Canals) | Workbench Python per canali, Manning, profili, paratoie, sifoni e risalti; verificare l'accuratezza dei singoli moduli. | Strumento specialistico |
| **GRAIN** | [UW-SASWE/GRAIN](https://github.com/UW-SASWE/GRAIN) | Dataset GIS mondiale dei canali irrigui; non è un simulatore idraulico. | Dataset di ricerca |
| **2DSOILRunoff** | [DennisTimlin-USDA/2DSOILRunoff](https://github.com/DennisTimlin-USDA/2DSOILRunoff) | Simulazione di infiltrazione e ruscellamento; progetto con aggiornamenti meno recenti. | Codice di ricerca |

### Idrologia, falde e analisi GIS

| Progetto | Repository | Applicazioni e limiti | Tipologia |
| --- | --- | --- | --- |
| **SPHY** | [FutureWater/SPHY](https://github.com/FutureWater/SPHY) | Modello idrologico distribuito per risorse idriche e scenari irrigui. | Modello scientifico |
| **SWAT+** | [swat-model/swatplus](https://github.com/swat-model/swatplus) | Modello di bacino per bilancio idrico, gestione agricola, erosione e qualità dell'acqua. | Modello scientifico |
| **pySWATPlus** | [swat-model/pySWATPlus](https://github.com/swat-model/pySWATPlus) | Libreria Python per gestire e automatizzare input e output SWAT+. | Libreria scientifica |
| **ParFlow** | [parflow/parflow](https://github.com/parflow/parflow) | Simulazione integrata di flussi superficiali e sotterranei. | Modello scientifico |
| **FloPy** | [modflowpy/flopy](https://github.com/modflowpy/flopy) | Libreria Python per modelli MODFLOW, falde e prelievi da pozzi. | Libreria scientifica |
| **pysheds** | [pysheds/pysheds](https://github.com/pysheds/pysheds) | Analisi di DEM, bacini e direzioni del deflusso. | Strumento GIS |

### Evapotraspirazione e irrigazione di precisione

| Progetto | Repository | Applicazioni e limiti | Tipologia |
| --- | --- | --- | --- |
| **pyTSEB** | [hectornieto/pyTSEB](https://github.com/hectornieto/pyTSEB) | Modelli di bilancio energetico a due sorgenti e dati termici per ET. | Modello scientifico |
| **SWIM-RS** | [dgketchum/swim-rs](https://github.com/dgketchum/swim-rs) | Bilancio idrico a scala di campo con dati satellitari e meteo. | Modello scientifico |
| **WaPOR Translator** | [TimHessels/WaporTranslator](https://github.com/TimHessels/WaporTranslator) | Indicatori FAO WaPOR su produttività dell'acqua e prestazioni irrigue; progetto meno recente. | Strumento di ricerca |
| **Hybrid Irrigation DSS** | [ascariolo/hybrid-model-irrigation-dss](https://github.com/ascariolo/hybrid-model-irrigation-dss) | Supporto sperimentale alla programmazione irrigua con modelli e machine learning. | Prototipo |
| **AmuFlow** | [mcpeblocker/amuflow](https://github.com/mcpeblocker/amuflow) | Uso sperimentale di dati satellitari e algoritmi per gestione irrigua. | Prototipo |

### Componentistica e simulazioni didattiche

| Progetto | Repository | Applicazioni e limiti | Tipologia |
| --- | --- | --- | --- |
| **OpenValve** | [fabiansteiner/OpenValve](https://github.com/fabiansteiner/OpenValve) | Valvola a pinza open hardware stampabile in 3D per controllo di liquidi e applicazioni irrigue. | Open hardware |
| **Green-Ampt Interactive Simulator** | [ziyaddmaa/Green-Ampt-Infiltration-Model-Interactive-Simulator](https://github.com/ziyaddmaa/Green-Ampt-Infiltration-Model-Interactive-Simulator) | Simulatore interattivo dell'infiltrazione secondo Green-Ampt; richiede verifica numerica. | Simulatore didattico |

### Criteri per l'utilizzo

- I modelli di bacino e falda integrano la progettazione irrigua, ma non sostituiscono il calcolo delle reti in pressione.
- Il catalogo non certifica la validazione scientifica dei programmi. Verificare equazioni, ipotesi, input, benchmark e affidabilità dei risultati.
- Per la riproducibilità dei calcoli annotare versione o commit utilizzato.
- I collegamenti non copiano codice: prima di integrare software esterno esaminare la relativa licenza.


## Quarta selezione: 20 repository aggiunti il 20 novembre 2026

Strumenti per idraulica delle reti, moto in canale, infiltrazione, modellazione delle colture, falde e telerilevamento. Ogni progetto resta nel repository del suo autore: i link non ne importano automaticamente il codice.

### Reti in pressione, pompe e regolazione

| Software | Repository | Applicazione | Pertinenza per l'irrigazione |
| --- | --- | --- | --- |
| **EPyT** | [OpenWaterAnalytics/EPyT](https://github.com/OpenWaterAnalytics/EPyT) | Toolkit Python per EPANET: portate, pressioni, pompe, valvole e scenari idraulici. | Alto |
| **EPyT-Flow** | [WaterFutures/EPyT-Flow](https://github.com/WaterFutures/EPyT-Flow) | Generazione di scenari e dati per simulazioni idrauliche di reti in pressione. | Alto |
| **EPyT-Control** | [WaterFutures/EPyT-Control](https://github.com/WaterFutures/EPyT-Control) | Sperimentazione di strategie di controllo e regolazione delle reti; non specifico per irrigazione. | Alto |
| **pandapipes** | [e2nIEE/pandapipes](https://github.com/e2nIEE/pandapipes) | Solver per reti di tubazioni di fluidi, di impiego generale; verificare le ipotesi per reti irrigue. | Medio |

### Canali, infiltrazione e drenaggio

| Software | Repository | Applicazione | Pertinenza per l'irrigazione |
| --- | --- | --- | --- |
| **HydroHP** | [marcusnobrega-eng/HydroHP](https://github.com/marcusnobrega-eng/HydroHP) | Moto vario monodimensionale con equazioni di Saint-Venant e metodi ai volumi finiti. | Alto |
| **OpenLISEM** | [vjetten/openlisem](https://github.com/vjetten/openlisem) | Modellazione di infiltrazione, deflusso superficiale ed erosione. | Alto |
| **LGAR-C / CASAM** | [NOAA-OWP/LGAR-C](https://github.com/NOAA-OWP/LGAR-C) | Infiltrazione Green-Ampt stratificata, redistribuzione e ruscellamento. | Alto |
| **PySWMM** | [pyswmm/pyswmm](https://github.com/pyswmm/pyswmm) | Interfaccia Python per reti di drenaggio e deflusso meteorico; non specifica per irrigazione. | Medio |
| **simsoil** | [arthur-e/simsoil](https://github.com/arthur-e/simsoil) | Modello semplificato del movimento verticale dell'acqua in una colonna di terreno. | Alto |

### Colture e fabbisogni irrigui

| Software | Repository | Applicazione | Pertinenza per l'irrigazione |
| --- | --- | --- | --- |
| **PCSE** | [ajwdewit/pcse](https://github.com/ajwdewit/pcse) | Ambiente Python di simulazione colturale, con processi di crescita e disponibilità idrica. | Alto |
| **DSSAT CSM** | [DSSAT/dssat-csm-os](https://github.com/DSSAT/dssat-csm-os) | Modelli di colture e interazioni suolo-pianta-atmosfera, gestione irrigua e produzione. | Alto |
| **PCSE-Gym** | [WUR-AI/PCSE-Gym](https://github.com/WUR-AI/PCSE-Gym) | Ambiente sperimentale per apprendimento per rinforzo nella gestione colturale. | Medio |
| **PyETo** | [woodcrafty/PyETo](https://github.com/woodcrafty/PyETo) | Calcolo Python dell'evapotraspirazione di riferimento; ultimo aggiornamento del progetto meno recente. | Medio |
| **ET-Demands / CropET** | [DOI-BOR/et-demands](https://github.com/DOI-BOR/et-demands) | Modello dei fabbisogni idrici delle colture con coefficiente colturale duale. | Alto |

### Falde e idrologia territoriale

| Software | Repository | Applicazione | Pertinenza per l'irrigazione |
| --- | --- | --- | --- |
| **MODFLOW 6** | [MODFLOW-ORG/modflow6](https://github.com/MODFLOW-ORG/modflow6) | Motore USGS per il flusso sotterraneo; integrazione naturale con FloPy gia' catalogato. | Alto |
| **Wflow.jl** | [Deltares/Wflow.jl](https://github.com/Deltares/Wflow.jl) | Modellazione idrologica distribuita per gestione della risorsa a scala territoriale. | Alto |
| **HydroMT** | [Deltares/hydromt](https://github.com/Deltares/hydromt) | Strumenti per costruire, configurare e analizzare modelli idrologici riproducibili. | Medio |
| **pywatershed** | [DOI-USGS/pywatershed](https://github.com/DOI-USGS/pywatershed) | Modello idrologico USGS in Python per simulare i processi del ciclo idrologico. | Alto |

### Telerilevamento e produttivita' dell'acqua

| Software | Repository | Applicazione | Pertinenza per l'irrigazione |
| --- | --- | --- | --- |
| **FAO pyWaPOR** | [un-fao/fao-wetl-pywapor](https://github.com/un-fao/fao-wetl-pywapor) | Stima satellitare di evaporazione, traspirazione e produzione di biomassa. | Alto |
| **WaPORIPA** | [wateraccounting/WaPORIPA](https://github.com/wateraccounting/WaPORIPA) | Indicatori WaPOR per la valutazione delle prestazioni e della produttivita' irrigua. | Alto |

**Valutazione preliminare:** la presenza nel catalogo non costituisce una validazione indipendente. Alcuni progetti sono modelli scientifici consolidati, altri sono interfacce, prototipi o strumenti di idrologia generale da adattare.

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

Questo repository contiene **documentazione, schede e uno script di recupero delle sorgenti esterne**, oltre ai collegamenti. Non contiene copie integrali dei 61 codici esterni, submodule Git o una pipeline che esegua automaticamente i progetti.
