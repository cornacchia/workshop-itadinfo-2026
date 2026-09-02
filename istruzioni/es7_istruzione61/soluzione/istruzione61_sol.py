"""
Istruzione 61

Il VALORE contenuto nelle cifre QUARTA e QUINTA dell'istruzione indica un canale di comunicazione
(ad esempio: terminale, file, stampante, ecc.). Il contenuto del REGISTRO indicato nella TERZA
cifra dell'istruzione è inviato a quel canale. Nella nostra simulazione questo vuol dire che
la funzione restituisce una coppia di valori di output dove il primo valore indica il CANALE
e il secondo valore indica il VALORE da stampare.
"""
def esegui_61 (indirizzo_istruzione, registri, memoria, istruzione_da_eseguire):
  # Il canale è identificato dalla quarta e quinta cifra
  id_canale = int(istruzione_da_eseguire[3:5])
  # Il valore da inviare al canale è indicato dalla terza cifra
  terza_cifra = int(istruzione_da_eseguire[2])

  output = (id_canale, registri[terza_cifra])

  return indirizzo_istruzione, registri, memoria, output