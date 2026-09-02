# https://docs.python.org/3/library/unittest.html
import unittest
from istruzione19 import esegui_19

class TestIstruzione19(unittest.TestCase):
  def test_1 (self):
    istruzione = '19213120000'
    registri = [0,0,0,0,0,0,0,0,0,0]
    memoria = [0 for _ in range(100)]
    indirizzo_istruzione, registri, memoria, output = esegui_19(1, registri, memoria, istruzione)
    self.assertEqual(registri[2], 1312, 'Il valore finale contenuto nel registro non  corretto.')

  def test_2 (self):
      istruzione = '1920042000'
      registri = [0,0,0,0,0,0,0,0,0,0]
      memoria = [0 for _ in range(100)]
      indirizzo_istruzione, registri, memoria, output = esegui_19(1, registri, memoria, istruzione)
      self.assertEqual(registri[2], 42, 'Il valore finale contenuto nel registro non  corretto.')


if __name__ == '__main__':
  unittest.main()