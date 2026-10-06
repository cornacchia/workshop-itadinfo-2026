"""
Istruzione 12

Somma il CONTENUTO DEL REGISTRO indicato nella QUARTA cifra dell'istruzione
al VALORE contenuto nella QUINTA cifra e usa il risultato come INDIRIZZO.
Copia il contenuto della MEMORIA all'INDIRIZZO calcolato nei passaggi precedenti
nel REGISTRO indicato dalla TERZA cifra dell'istruzione.
"""

def esegui_12 (indirizzo_istruzione, registri, memoria, istruzione_da_eseguire):
  registro_terza_cifra = int(istruzione_da_eseguire[2])
  registro_quarta_cifra = int(istruzione_da_eseguire[3])
  valore_quinta_cifra = int(istruzione_da_eseguire[4])

  # Somma il CONTENUTO DEL REGISTRO indicato nella QUARTA cifra dell'istruzione
  # al VALORE contenuto nella QUINTA cifra e usa il risultato come INDIRIZZO.
  indirizzo_memoria = registri[registro_quarta_cifra] + valore_quinta_cifra

  # Copia il contenuto della MEMORIA all'INDIRIZZO calcolato nei passaggi precedenti
  # nel REGISTRO indicato dalla TERZA cifra dell'istruzione.
  valore_memoria = memoria[indirizzo_memoria]
  registri[registro_terza_cifra] = valore_memoria

  return indirizzo_istruzione, registri, memoria, (-1, -1)