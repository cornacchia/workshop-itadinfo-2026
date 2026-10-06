"""
Istruzione 01

Stop. Interrompe la simulazione scrivendo il valore -1
sull'indirizzo istruzione.
"""
def esegui_01 (indirizzo_istruzione, registri, memoria, istruzione_da_eseguire):
  # Scrivere -1 sull'indirizzo istruzione interrompe la simulazione
  indirizzo_istruzione = -1

  return indirizzo_istruzione, registri, memoria, (-1, -1)