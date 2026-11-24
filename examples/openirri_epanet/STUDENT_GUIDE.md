# Laboratorio: verifica riproducibile OpenIrri--EPANET 2.2

## Obiettivo

Analizzare **solo l'idraulica di rete** di un impianto fisso ad aspersione
in regime permanente. Confrontare due diametri interni delle ali, distinguendo
rigorosamente il calcolo analitico dalla soluzione del solver EPANET 2.2.
L'esercitazione **non** calcola CU, DU o uniformita' pluviometrica.

## Dati e ipotesi

Usare i file `case_55p4.inp`, `case_66p0.inp` e `expected_analytic.json`.
Il sistema comprende 4 ali, ciascuna con 32 irrigatori da 0.52 m3/h,
32 tratti da 12.6 m per ala, 270 m di condotta principale con diametro
interno 176 mm, 4 tratti da 30 m di sottoprincipale con diametro 110 mm,
C = 150 e domanda imposta (DDA). Le quote degli irrigatori sono 7, 8,
9 e 10 m per le ali 1--4. La curva di pompa sintetica e':

`H [m] = 61 - 0.0025 * (Q [m3/h])**2`.

**Attenzione alla differenza dal testo originario:** il modello EPANET
pubblicato in questa cartella comprende anche quattro derivazioni
`DER1`--`DER4` di 1 m (diametro 110 mm). Questi tratti causano una
perdita di circa 0.0022 m nel ramo sfavorito; non eliminarli quando si
confrontano i risultati qui pubblicati.

## Procedura ripetibile

1. Dalla radice del repository, lanciare `python3 examples/openirri_epanet/check_case.py`.
   Lo script verifica che gli input siano identici alle versioni generate,
   ricostruisce portate e pressioni, e confronta i risultati con il JSON.
2. Eseguire `python3 -m unittest discover -s examples/openirri_epanet/tests -v`.
   Non servono pacchetti Python esterni per queste verifiche.
3. Per eseguire il solver, creare un ambiente **Python 3.11** e installare
   `python -m pip install -r examples/openirri_epanet/requirements-epanet.txt`.
4. Trovare la libreria EPANET 2.2 fornita da WNTR, per esempio su Linux:

   ```sh
   python -c "from pathlib import Path; import sysconfig; print(next(Path(sysconfig.get_paths()['purelib']).glob('wntr/epanet/libepanet/linux-x64/libepanet22.so')))"
   ```

5. Sostituire `<LIBRERIA>` con il percorso ottenuto e lanciare:

   ```sh
   python3 examples/openirri_epanet/check_case.py --epanet-lib "<LIBRERIA>" --solver-output solver_2_2.json
   ```

   Lo script rifiuta un solver di versione diversa da 2.2 e impone le
   tolleranze documentate nel README. In alternativa, la GitHub Action
   `OpenIrri-EPANET 2.2 hydraulic reproduction` conserva un JSON e il log
   di esecuzione come artefatti della run.

## Valori analitici attesi (non EPANET)

| Quantita' | D = 55.4 mm | D = 66.0 mm |
|---|---:|---:|
| Portata totale (m3/h) | 66.560000 | 66.560000 |
| Perdita principale (m) | 0.783573 | 0.783573 |
| Perdita sottoprincipale (m) | 1.666715 | 1.666715 |
| Perdita ultima derivazione DER4 (m) | 0.002197 | 0.002197 |
| Perdita ultima ala (m) | 9.160905 | 3.905278 |
| Prevalenza pompa (m) | 49.924416 | 49.924416 |
| Pressione minima al nodo L4_32 (m) | 28.311027 | 33.566654 |

## Questioni per gli studenti

- Dimostrare per continuita' che la portata all'ingresso e' 66.56 m3/h.
- Ricavare la portata in ciascuno dei 32 tratti dell'ala.
- Calcolare il fattore di riduzione **idraulico** F di Christiansen tramite
  la somma discreta e confrontarlo con la formula approssimata OpenIrri.
- Individuare il nodo di minima pressione e quantificare il margine
  sulla soglia illustrativa di 28 m c.a. nei due casi.
- Spiegare perche' EPANET e la formula SI con coefficienti 10.67 e 4.87
  possono mostrare minimi scostamenti numerici.
- Discutere perche' il soddisfacimento della pressione minima **non**
  permette di concludere che l'uniformita' di irrigazione sia adeguata.

## Requisiti per una relazione tecnica verificabile

Registrare versione EPANET Toolkit, versione WNTR, Python, sistema operativo,
commit Git, file `.inp` eseguito, risultati analitici, risultati del solver,
scostamenti con segno, e soglie di accettazione. Distinguere le formule
ricostruite dal benchmark pubblico OpenIrri dall'esecuzione diretta di OpenIrri.

Fonti: [esercitazione e modello](README.md),
[OpenIrri](https://github.com/El-Naggar8876/openirri),
[EPANET 2.2](https://usepa.github.io/EPANET2.2/).
