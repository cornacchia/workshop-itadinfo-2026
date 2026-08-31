# https://docs.python.org/3/library/unittest.html
import unittest
import random
from memoria import inizializza_memoria

class TestMemoria(unittest.TestCase):
  def test_restituisce_lista(self):
    mem = inizializza_memoria(10)
    self.assertIsInstance(mem, list, 'La funzione inizializza_memoria non restituisce una lista')

  def test_lunghezza(self):
    for _ in range(10):
      random_length = random.randrange(1, 1000)
      mem = inizializza_memoria(random_length)
      self.assertEqual(len(mem), random_length, 'La lunghezza della lista non è uguale al parametro dimensione passato alla funzione.')

  def test_valori(self):
    for _ in range(10):
      random_length = random.randrange(1, 1000)
      mem = inizializza_memoria(random_length)
      self.assertTrue(len(mem) > 0, 'La lista restituita non contiene elementi.')
      for el in mem:
        self.assertEqual(el, 0, 'La lista restituita contiene elementi diversi da 0.')

if __name__ == '__main__':
  unittest.main()