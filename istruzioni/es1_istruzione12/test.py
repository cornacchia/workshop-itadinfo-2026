# https://docs.python.org/3/library/unittest.html
import unittest
from istruzione12 import esegui_12

class TestIstruzione12(unittest.TestCase):
  def test_1 (self):
    istruzione = '1263700000'
    registri = [0,0,0,13,0,0,0,0,0,0]
    memoria = [0 for _ in range(100)]
    # Indirizzo atteso: 13 + 7 = 20
    memoria[20] = 42
    indirizzo_istruzione, registri, memoria, output = esegui_12(1, registri, memoria, istruzione)
    self.assertEqual(registri[6], 42, 'Il valore finale contenuto nel registro non  corretto.')

  def test_2 (self):
      istruzione = '1263000000'
      registri = [0,0,0,0,0,0,0,0,0,0]
      memoria = [0 for _ in range(100)]
      # Indirizzo atteso: 0 + 0 = 0
      memoria[0] = 13
      indirizzo_istruzione, registri, memoria, output = esegui_12(1, registri, memoria, istruzione)
      self.assertEqual(registri[0], 13, 'Il valore finale contenuto nel registro non  corretto.')



if __name__ == '__main__':
  unittest.main()