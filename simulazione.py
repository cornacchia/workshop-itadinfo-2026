from parte1_es1_registri.registri import inizializza_registri
from parte1_es2_memoria.memoria import inizializza_memoria
from parte2_es1_leggi_programma.leggi_programma import leggi_programma_in_memoria
from parte2_es2_dscii.dscii import inizializza_dscii
from parte3_istruzioni.esegui_istruzione import esegui_istruzione

dscii = None

def avvia_simulazione ():
  global dscii

  print("=== AVVIO SIMULAZIONE ===")
  indirizzo_istruzione = 0
  registri = inizializza_registri()
  memoria = inizializza_memoria(100)
  memoria = leggi_programma_in_memoria('./programma.txt', memoria)
  dscii = inizializza_dscii()

  while indirizzo_istruzione >= 0:
    indirizzo_istruzione, registri, memoria, output = esegui_istruzione(indirizzo_istruzione, registri, memoria)
    # Il primo valore contenuto nella coppia OUTPUT (output[0]) indica
    # un canale di comunicazione. Il codice 1 indica il terminale.
    if (output[0] == 1):
      # Il secondo valore contenuto nella coppia OUTPUT (output[1])
      # indica il codice DSCII di un carattere da stampare.
      # L'opzione end='' serve per evitare che print vada a capo
      # automaticamente (infatti vogliamo andare a capo solo se l'output
      # contiene un carattere a capo)
      print(dscii[output[1]], end='')

  print("\n=== SIMULAZIONE TERMINATA ===")

avvia_simulazione()