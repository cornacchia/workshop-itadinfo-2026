# https://docs.python.org/3/library/unittest.html
import unittest
from registri import inizializza_registri

class TestRegistri(unittest.TestCase):
  def test_restituisce_lista(self):
    reg = inizializza_registri()
    self.assertIsInstance(reg, list, 'La funzione inizializza_registri non restituisce una lista')

  def test_lunghezza(self):
    reg = inizializza_registri()
    self.assertEqual(len(reg), 10, 'La lunghezza della lista non è uguale a 10.')

  def test_valori(self):
    reg = inizializza_registri()
    self.assertTrue(len(reg) > 0, 'La lista restituita non contiene elementi.')
    for el in reg:
      self.assertEqual(el, 0, 'La lista restituita contiene elementi diversi da 0.')

if __name__ == '__main__':
  unittest.main()