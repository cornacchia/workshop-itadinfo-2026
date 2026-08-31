from soluzione.registri_sol import inizializza_registri as inizializza_registri_soluzione
from registri import inizializza_registri as inizializza_registri_esercizio

registri_soluzione = None
try:
  registri_soluzione = inizializza_registri_soluzione()
  if not isinstance(registri_soluzione, list):
    print('!!! Errore a monte (soluzione fornita dal laboratorio): la funzione non restituisce una lista.')
  else:
    if len(registri_soluzione) != 10:
      print('!!! Errore a monte (soluzione fornita dal laboratorio): la lista dei registri ha lunghezza diversa da 10.')

    soluzione_all_zeros = True
    for el in registri_soluzione:
      if el != 0:
        soluzione_all_zeros = False
    if not soluzione_all_zeros:
      print('!!! Errore a monte (soluzione fornita dal laboratorio): la lista dei registri contiene elementi diversi da 0.')
except:
  print('!!! Errore a monte (soluzione fornita dal laboratorio): la funzione causa un errore a tempo di esecuzione.')



passed_tests = 0

registri_esercizio = None
try:
  registri_esercizio = inizializza_registri_esercizio()
  print('[0] Test riuscito: la funzione non causa errori a tempo di esecuzione.')
  passed_tests += 1

  if not isinstance(registri_esercizio, list):
    print('!!! [1] Test fallito: la funzione non restituisce una lista.')
  else:
    print('[1] Test riuscito: la funzione restituisce una lista.')
    passed_tests += 1

    if len(registri_esercizio) != 10:
      print('!!! [2] Test fallito: la lista dei registri ha lunghezza diversa da 10.')
    else:
      print('[2] Test riuscito: la lista dei registri ha lunghezza 10.')
      passed_tests += 1

    esercizio_all_zeros = len(registri_esercizio) > 0
    for el in registri_esercizio:
      if el != 0:
        esercizio_all_zeros = False
    if not esercizio_all_zeros:
      print('!!! [3] Test fallito: la lista dei registri non contiene solo elementi uguali a 0.')
    else:
      print('[3] Test riuscito: la lista contiene solo valori interi uguali a 0.')
      passed_tests += 1
except:
  print('!!! [0] Test fallito: la funzione causa un errore a tempo di esecuzione.')


print('Totale test riusciti: ' + str(passed_tests) + ' / 4')