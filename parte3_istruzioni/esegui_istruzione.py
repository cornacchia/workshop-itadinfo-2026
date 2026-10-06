from parte3_es4_istruzione01.istruzione01 import esegui_01
from parte3_es1_istruzione12.istruzione12 import esegui_12
from parte3_es2_istruzione19.istruzione19 import esegui_19
from parte3_es3_istruzione21.istruzione21 import esegui_21
from parte3_es5_istruzione44.istruzione44 import esegui_44
from parte3_es6_istruzione52.istruzione52 import esegui_52
from parte3_es7_istruzione61.istruzione61 import esegui_61

def converti_a_dieci_cifre (valore_intero):
  valore_stringa = str(valore_intero)
  # Aggiunge 0 all'inizio della stringa fino
  # a che non è lunga esattamente 10 cifre
  while len(valore_stringa) < 10:
    valore_stringa = '0' + valore_stringa
  return valore_stringa

def esegui_istruzione (indirizzo_istruzione, registri, memoria):
  # Recupera l'istruzione da eseguire dalla memoria
  istruzione_da_eseguire = converti_a_dieci_cifre(memoria[indirizzo_istruzione])
  # Estrae il codice identificativo (id) dell'istruzione
  # salvato nelle prime due cifre
  id_istruzione = int(istruzione_da_eseguire[0:2])

  # Aggiunge 1 all'indirizzo istruzione
  indirizzo_istruzione = indirizzo_istruzione + 1

  if id_istruzione == 1:
    return esegui_01(indirizzo_istruzione, registri, memoria, istruzione_da_eseguire)
  elif id_istruzione == 12:
    return esegui_12(indirizzo_istruzione, registri, memoria, istruzione_da_eseguire)
  elif id_istruzione == 19:
    return esegui_19(indirizzo_istruzione, registri, memoria, istruzione_da_eseguire)
  elif id_istruzione == 21:
    return esegui_21(indirizzo_istruzione, registri, memoria, istruzione_da_eseguire)
  elif id_istruzione == 44:
    return esegui_44(indirizzo_istruzione, registri, memoria, istruzione_da_eseguire)
  elif id_istruzione == 52:
    return esegui_52(indirizzo_istruzione, registri, memoria, istruzione_da_eseguire)
  elif id_istruzione == 61:
    return esegui_61(indirizzo_istruzione, registri, memoria, istruzione_da_eseguire)
  else:
    print(id_istruzione, 'non definito in questa simulazione!')
    return -1, registri, memoria, (-1, -1)