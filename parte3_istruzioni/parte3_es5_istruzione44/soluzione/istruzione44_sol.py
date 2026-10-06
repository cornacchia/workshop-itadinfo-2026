"""
Istruzione 44

Controlla se il CONTENUTO del REGISTRO indicato dalla TERZA cifra dell'istruzione è zero.
Se è zero, copia il VALORE contenuto nelle cifre dalla QUARTA alla DECIMA dell'istruzione
(estremi compresi) nell'INDIRIZZO ISTRUZIONE.
Questa è una istruzione di "salto" condizionale che permette, ad esempio, di implementare cicli.
"""
def esegui_44 (indirizzo_istruzione, registri, memoria, istruzione_da_eseguire):
  terza_cifra = int(istruzione_da_eseguire[2])
  valore_terza_cifra = registri[terza_cifra]

  # Controlla se il CONTENUTO del REGISTRO indicato dalla TERZA cifra dell'istruzione è zero.
  if valore_terza_cifra == 0:
    # Se è zero, copia il VALORE contenuto nelle cifre
    # dalla QUARTA alla DECIMA dell'istruzione (estremi compresi) ...
    valore_quarta_decima = int(istruzione_da_eseguire[3:])
    # ... nell'INDIRIZZO ISTRUZIONE
    indirizzo_istruzione = valore_quarta_decima

  return indirizzo_istruzione, registri, memoria, (-1, -1)