"""
Istruzione 21
Somma il CONTENUTO del REGISTRO indicato dalla QUARTA cifra dell'istruzione
al VALORE contenuto nella QUINTA cifra dell'istruzione.
Copia il risultato nel REGISTRO indicato dalla TERZA cifra dell'istruzione.
"""

def esegui_21 (indirizzo_istruzione, registri, memoria, istruzione_da_eseguire):
  terza_cifra = int(istruzione_da_eseguire[2])
  quarta_cifra = int(istruzione_da_eseguire[3])
  quinta_cifra = int(istruzione_da_eseguire[4])

  valore_registro_quarta_cifra = int(registri[quarta_cifra])

  # Somma il CONTENUTO del REGISTRO indicato dalla QUARTA cifra dell'istruzione
  # al VALORE contenuto nella QUINTA cifra dell'istruzione.
  risultato = valore_registro_quarta_cifra + quinta_cifra

  # Copia il risultato nel REGISTRO indicato dalla TERZA cifra dell'istruzione.
  registri[terza_cifra] = risultato

  return indirizzo_istruzione, registri, memoria, (-1, -1)