# https://docs.python.org/3/library/unittest.html
import unittest
from istruzione21 import esegui_21

class TestIstruzione21(unittest.TestCase):
  def test_1 (self):
    istruzione = '21743000000'
    registri = [0,0,0,0,6,0,0,0,0,0]
    # Valore atteso 6 + 3 = 9
    memoria = [0 for _ in range(100)]
    indirizzo_istruzione, registri, memoria, output = esegui_21(1, registri, memoria, istruzione)
    self.assertEqual(registri[7], 9, 'Il valore finale contenuto nel registro non  corretto.')

if __name__ == '__main__':
  unittest.main()