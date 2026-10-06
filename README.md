# workshop-itadinfo-2026

Il file per l'esercitazione interattiva è disponibile [a questo link](https://colab.research.google.com/drive/1QWfKT9fjl-duKuaWWIIu1QObI0bmE1uZ#scrollTo=tFIg0LWiMYMb&forceEdit=true&sandboxMode=true) (per aprirlo serve un account Google).
Le soluzioni degli esercizi sono invece disponibili [a questo link](https://colab.research.google.com/drive/1ypUS-LWfELBW8j1f0sQLQE8BUkNADxK8?usp=sharing).

In alternativa potete lavorare al progetto localmente copiandolo con il comando ```git clone https://github.com/cornacchia/workshop-itadinfo-2026```.
Tutti gli script vanno eseguiti dalla radice del progetto (la cartella ```workshop-itadinfo-2026```): per esempio, per eseguire i test degli esercizi sulla **memoria** eseguire ```python3 ./parte1_es2_memoria/test.py```.
I file con le soluzioni degli esercizi sono nelle cartelle chiamate ```soluzione``` (una per ogni esercizio) e hanno nomi che terminano con suffisso ```_sol.py```.

Una volta terminati tutti gli esercizi potete eseguire la simulazione con il comando ```python3 ./simulazione.py```. Verrà eseguita una simulazione di computer che esegue il programma in linguaggio macchina salvato nel file ```./programma.txt```.

La cartella `./gates` contiene uno script che mostra come implementare memoria e registri a partire da operatori logici elementari. Per implementare una cella di memoria che salva 1 bit sono necessari AND e NOT, che possono essere combinati in NAND, che a sua volta può essere usato per implementare un circuito FLIP-FLOP di tipo D. Mettendo insieme più circuiti di questo tipo è possibile implementare memoria e registri a un livello di astrazione più basso rispetto a quanto fatto in ```./parte1_es2_memoria/memoria.py``` e ```./parte1_es1_registri/registri.py```.