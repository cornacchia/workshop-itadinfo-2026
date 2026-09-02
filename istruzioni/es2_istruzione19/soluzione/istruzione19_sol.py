"""
Istruzione 19

Copia il VALORE indicato nelle cifre dalla QUARTA alla DECIMA dell'istruzione
(estremi compresi) nel REGISTRO indicato dalla TERZA cifra dell'istruzione.
"""
def esegui_19 (indirizzo_istruzione, registri, memoria, istruzione_da_eseguire):
  registro_terza_cifra = int(istruzione_da_eseguire[2])
  valore_quarta_decima = int(istruzione_da_eseguire[3:])

  registri[registro_terza_cifra] = valore_quarta_decima

  return indirizzo_istruzione, registri, memoria, (-1, -1)