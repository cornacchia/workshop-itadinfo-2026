# https://docs.python.org/3/library/unittest.html
import unittest
from istruzione44 import esegui_44

class TestIstruzione44(unittest.TestCase):
  def test_1 (self):
    istruzione = '441000000042'
    # Condizione non verificata
    registri = [0,4,0,0,0,0,0,0,0,0]
    memoria = [0 for _ in range(100)]
    indirizzo_istruzione, registri, memoria, output = esegui_44(1, registri, memoria, istruzione)
    self.assertNotEqual(indirizzo_istruzione, 42, 'Il valore finale dell\'indirizzo istruzione non è corretto.')

  def test_2 (self):
    istruzione = '445000000042'
    # Condizione verificata
    registri = [0,5,0,0,4,0,0,0,0,0]
    memoria = [0 for _ in range(100)]
    indirizzo_istruzione, registri, memoria, output = esegui_44(1, registri, memoria, istruzione)
    self.assertEqual(indirizzo_istruzione, 42, 'Il valore finale dell\'indirizzo istruzione non è corretto.')

if __name__ == '__main__':
  unittest.main()