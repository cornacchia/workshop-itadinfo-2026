"""
PRIMM è un acronimo che indica una sequenza di operazioni per analizzare e modificare un programma.
Predict - Leggi il programma e prevedi quale sarà l'esito della sua esecuzione
Run - Esegui il programma e verifica la correttezza della tua previsione
Investigate - Analizza il programma, approfondisci alcuni suoi aspetti,
              identifica eventuali errori/mancanze/miglioramenti possibili
Modify - Modifica il programma per raggiungere un obiettivo
Make - Crea un nuovo programma usando i concetti appresi durante le fasi precedenti
"""

"""
Formulazione del problema:
Scrivi una funzione chiamata "leggi_programma_in_memoria" che accetti come parametri
il nome di un file e il riferimento alla memoria della simulazione.
Possiamo assumere che il file conterrà un programma in linguaggio macchina,
ogni riga del file corrisponde a una singola istruzione.
La funzione deve leggere le istruzioni e copiarle in ordine nelle celle della memoria
della simulazione, una istruzione per cella, a partire dalla cella numero 0.
"""

def leggi_programma_in_memoria (nome_file, memoria):
  with open(nome_file, 'r') as file_programma:
    contenuto = file_programma.read()
    lista_contenuto = contenuto.split('\n')
    for i in range(5):
      print(lista_contenuto[i])
  return memoria

# Le righe successive servono per le fasi predict/run
# Commentarle alla fine dell'esercizio
memoria = [0 for i in range(100)]
leggi_programma_in_memoria('./leggi_programma/materiale_test/programma2.txt', memoria)