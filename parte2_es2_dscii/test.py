# https://docs.python.org/3/library/unittest.html
import unittest
from dscii import inizializza_dscii

class TestDSCII(unittest.TestCase):
  def test_dizionario(self):
    dscii = inizializza_dscii()
    self.assertIsInstance(dscii, dict, 'La funzione inizializza_dscii non restituisce un dizionario.')

  def test_lunghezza(self):
    dscii = inizializza_dscii()
    self.assertEqual(len(dscii), 100, 'Il dizionario non ha 100 chiavi e valori.')

  def test_spazio(self):
    dscii = inizializza_dscii()
    self.assertEqual(dscii[5], ' ', 'Il carattere di spazio non è salvato correttamente.')

  def test_caratteri(self):
    dscii = inizializza_dscii()
    self.assertEqual(dscii[10], '%', 'Un carattere non è stato salvato correttamente')
    self.assertEqual(dscii[21], '0', 'Un carattere non è stato salvato correttamente')
    self.assertEqual(dscii[26], '5', 'Un carattere non è stato salvato correttamente')
    self.assertEqual(dscii[41], 'D', 'Un carattere non è stato salvato correttamente')
    self.assertEqual(dscii[68], '_', 'Un carattere non è stato salvato correttamente')
    self.assertEqual(dscii[74], 'e', 'Un carattere non è stato salvato correttamente')
    self.assertEqual(dscii[81], 'l', 'Un carattere non è stato salvato correttamente')
    self.assertEqual(dscii[90], 'u', 'Un carattere non è stato salvato correttamente')
    self.assertEqual(dscii[94], 'y', 'Un carattere non è stato salvato correttamente')
    self.assertEqual(dscii[96], '{', 'Un carattere non è stato salvato correttamente')

if __name__ == '__main__':
  unittest.main()