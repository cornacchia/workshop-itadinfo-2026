# https://docs.python.org/3/library/unittest.html
import unittest
from istruzione52 import esegui_52

class TestIstruzione52(unittest.TestCase):
  def test_1 (self):
    istruzione = '521000000042'
    registri = [0,4,0,0,0,0,0,0,0,0]
    memoria = [0 for _ in range(100)]
    indirizzo_istruzione, registri, memoria, output = esegui_52(1, registri, memoria, istruzione)
    self.assertEqual(indirizzo_istruzione, 42, 'Il valore finale dell\'indirizzo istruzione non è corretto.')

  def test_2 (self):
    istruzione = '525000000013'
    registri = [0,5,0,0,4,0,0,0,0,0]
    memoria = [0 for _ in range(100)]
    indirizzo_istruzione, registri, memoria, output = esegui_52(1, registri, memoria, istruzione)
    self.assertEqual(indirizzo_istruzione, 13, 'Il valore finale dell\'indirizzo istruzione non è corretto.')

if __name__ == '__main__':
  unittest.main()