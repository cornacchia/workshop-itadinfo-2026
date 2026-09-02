# https://docs.python.org/3/library/unittest.html
import unittest
from istruzione01 import esegui_01

class TestIstruzione01(unittest.TestCase):
  def test_1 (self):
    istruzione = '01000000000'
    registri = [0,0,0,0,0,0,0,0,0,0]
    memoria = [0 for _ in range(100)]
    indirizzo_istruzione, registri, memoria, output = esegui_01(1, registri, memoria, istruzione)
    self.assertEqual(indirizzo_istruzione, -1, 'Il valore finale dell\'indirizzo istruzione non è corretto.')

if __name__ == '__main__':
  unittest.main()