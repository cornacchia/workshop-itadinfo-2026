"""
Istruzione 52

Copia il VALORE indicato nelle cifre dalla QUARTA alla DECIMA dell'istruzione
(estremi compresi) nell'INDIRIZZO ISTRUZIONE.
Questa è una istruzione di "salto" non condizionale, che può essere usata ad esempio
per eseguire procedure.
"""

def esegui_52 (indirizzo_istruzione, registri, memoria, istruzione_da_eseguire):
  valore_quarta_decima = int(istruzione_da_eseguire[3:])
  indirizzo_istruzione = valore_quarta_decima

  return indirizzo_istruzione, registri, memoria, (-1, -1)