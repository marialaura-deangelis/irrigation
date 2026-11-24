# Come trovare e utilizzare il materiale

## Che cosa e' stato caricato su GitHub

1. [README.md](../README.md): indice generale con i 61 repository esterni.
2. [docs/CATALOGO_COMPLETO.md](CATALOGO_COMPLETO.md): tabella unica di tutti i 61 progetti.
3. [docs/NUOVI_20_PROGETTI.md](NUOVI_20_PROGETTI.md): schede sintetiche dei 20 progetti dell'ultima ricerca.
4. [examples/README.md](../examples/README.md): traccia didattica del confronto OpenIrri e calcolo analitico, predisposto anche per EPANET.
5. [scripts/scarica_repositories.py](../scripts/scarica_repositories.py): strumento per clonare sul computer i repository selezionati.
6. [LICENSE-CC-BY-4.0.md](../LICENSE-CC-BY-4.0.md): condizioni per il riutilizzo dei testi e dei materiali didattici originali sotto CC BY 4.0, esclusi i contenuti di terzi.
7. [LICENSE-MIT](../LICENSE-MIT): licenza MIT applicabile allo script Python originale `scripts/scarica_repositories.py`.
8. [docs/references/openirri.bib](references/openirri.bib): citazioni BibTeX dell'articolo scientifico OpenIrri in *SoftwareX* e dell'archivio software Zenodo v1.0.2.

## Che cosa non e' stato caricato

Non sono stati importati i sorgenti dei 61 software esterni, ne' create copie, fork o submodule. Avere il link al repository di terzi non trasferisce il suo contenuto in questa cartella. Ogni progetto mantiene storia, licenza e manutenzione proprie.

## Dove si vedono i file in GitHub

Aprire https://github.com/marialaura-deangelis/irrigation e selezionare il branch main. Nella scheda Code compaiono README.md e le cartelle docs, examples e scripts. Il README viene mostrato anche sotto l'elenco dei file.

I file di licenza si trovano nella radice del repository; la bibliografia BibTeX e' nella sottocartella `docs/references/`.

## Come consultare un progetto

Dal catalogo, aprire il link GitHub del progetto. Nella sua pagina e' possibile leggere il README, visualizzare il codice e scaricarlo usando Code > Download ZIP.

## Come scaricare i sorgenti con lo script

Prerequisiti: Python 3 e Git installati sul computer. Lo script usa solo librerie standard di Python; per scaricare e' necessaria una connessione Internet.

Da una copia locale di questo repository, eseguire:

    python scripts/scarica_repositories.py --list
    python scripts/scarica_repositories.py --repo OpenWaterAnalytics/EPyT
    python scripts/scarica_repositories.py --repo El-Naggar8876/openirri --repo OpenWaterAnalytics/EPANET

Per clonare tutti e 61 i repository (operazione potenzialmente grande):

    python scripts/scarica_repositories.py --all

Lo script non sovrascrive cartelle esistenti e salva i progetti nella directory locale repository_esterni, esclusa da Git tramite .gitignore.

## Attenzione a licenze e sicurezza

Il download di software esterno non implica autorizzazione a ripubblicarlo o incorporarlo in un unico prodotto. Esaminare le licenze e non eseguire script, installer o workflow di provenienza non verificata. Lo script scarica i repository ma non esegue il loro codice.

## Stato del caso OpenIrri / EPANET

Il materiale didattico del confronto numerico e' sintetizzato in examples/README.md. I risultati EPANET non sono stati ottenuti con il solver ufficiale: i valori sono riferiti ai calcoli analitici e alle formule implementate da OpenIrri.
