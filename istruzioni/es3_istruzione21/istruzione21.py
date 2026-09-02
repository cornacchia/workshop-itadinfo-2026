"""
Istruzione 21
Somma il CONTENUTO del REGISTRO indicato dalla QUARTA cifra dell'istruzione
al VALORE contenuto nella QUINTA cifra dell'istruzione.
Copia il risultato nel REGISTRO indicato dalla TERZA cifra dell'istruzione.
"""

"""
Problema a completamento.
Il codice già fornito non va modificato. Serve solo aggiungere
una o più istruzioni dove indicato.
"""

def esegui_21 (indirizzo_istruzione, registri, memoria, istruzione_da_eseguire):
  terza_cifra = int(istruzione_da_eseguire[2])
  quarta_cifra = int(istruzione_da_eseguire[3])
  quinta_cifra = int(istruzione_da_eseguire[4])

  # Aggiungere codice qui

  return indirizzo_istruzione, registri, memoria, (-1, -1)