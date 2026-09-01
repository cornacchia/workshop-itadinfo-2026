def inizializza_dscii ():
  dscii = {}
  with open('./dscii/dscii.txt', 'r') as file_dscii:
    contenuto = file_dscii.read()
    lista_contenuto = contenuto.split('\n')
    for i in range(len(lista_contenuto)):
      riga = lista_contenuto[i]
      codice = int(riga[0:2])
      valore = riga[2:].strip()
      if valore == '[spazio]':
        valore = ' '
      dscii[codice] = valore
  return dscii