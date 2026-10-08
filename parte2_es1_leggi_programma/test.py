# https://docs.python.org/3/library/unittest.html
import unittest
from leggi_programma import leggi_programma_in_memoria

class TestLeggiProgramma(unittest.TestCase):
  def test_programma_1(self):
    memoria = [0 for i in range(100)]
    leggi_programma_in_memoria('./parte2_es1_leggi_programma/materiale_test/programma1.txt', memoria)
    for i in range(1, 6):
      self.assertEqual(memoria[i-1], i, 'La funzione non ha copiato correttamente una istruzione.')
    for i in range(6, len(memoria)):
      self.assertEqual(memoria[i], 0, 'La funzione ha scritto aree di memoria in eccesso.')

  def test_programma_2(self):
      memoria = [0 for i in range(100)]
      leggi_programma_in_memoria('./parte2_es1_leggi_programma/materiale_test/programma2.txt', memoria)
      for i in range(1, 9):
        self.assertEqual(memoria[i-1], i, 'La funzione non ha copiato correttamente una istruzione.')
      for i in range(9, len(memoria)):
        self.assertEqual(memoria[i], 0, 'La funzione ha scritto aree di memoria in eccesso.')

  def test_programma_3(self):
        memoria = [0 for i in range(100)]
        leggi_programma_in_memoria('./parte2_es1_leggi_programma/materiale_test/programma3.txt', memoria)
        for i in range(len(memoria)):
          self.assertEqual(memoria[i], 0, 'La funzione ha scritto aree di memoria in eccesso.')

if __name__ == '__main__':
  unittest.main()