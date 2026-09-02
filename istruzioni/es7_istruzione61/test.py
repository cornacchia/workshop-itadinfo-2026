# https://docs.python.org/3/library/unittest.html
import unittest
from istruzione61 import esegui_61

class TestIstruzione61(unittest.TestCase):
  def test_1 (self):
    registri = [0,0,42,0,0,0,0,0,0,0]
    memoria = [0 for _ in range(100)]
    istruzione = '6120100000'
    indirizzo_istruzione, registri, memoria, output = esegui_61(1, registri, memoria, istruzione)
    self.assertEqual(output[0], 1, 'Il canale di comunicazione restituito non è corretto.')
    self.assertEqual(output[1], 42, 'Il valore da inviare al canale di comunicazione non è corretto.')

  def test_2 (self):
      registri = [0,0,12,0,0,0,0,0,0,0]
      memoria = [0 for _ in range(100)]
      istruzione = '6121300000'
      indirizzo_istruzione, registri, memoria, output = esegui_61(1, registri, memoria, istruzione)
      self.assertEqual(output[0], 13, 'Il canale di comunicazione restituito non è corretto.')
      self.assertEqual(output[1], 12, 'Il valore da inviare al canale di comunicazione non è corretto.')

if __name__ == '__main__':
  unittest.main()