"""
Istruzione 19

Copia il VALORE indicato nelle cifre dalla QUARTA alla DECIMA dell'istruzione
(estremi compresi) nel REGISTRO indicato dalla TERZA cifra dell'istruzione.
"""

"""
Problema a completamento.
Il codice già fornito non va modificato. Serve solo aggiungere
una o più istruzioni dove indicato.
"""

def esegui_19 (indirizzo_istruzione, registri, memoria, istruzione_da_eseguire):
  registro_terza_cifra = int(istruzione_da_eseguire[2])
  valore_quarta_decima = int(istruzione_da_eseguire[3:])

  # Aggiungere codice qui

  return indirizzo_istruzione, registri, memoria, (-1, -1)