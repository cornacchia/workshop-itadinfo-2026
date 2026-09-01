from registri.registri import inizializza_registri
from memoria.memoria import inizializza_memoria
from leggi_programma.leggi_programma import leggi_programma_in_memoria
from dscii.dscii import inizializza_dscii

dscii = None

def avvia_simulazione ():
  global dscii

  program_counter = 0
  registri = inizializza_registri()
  memoria = inizializza_memoria(100)
  memoria = leggi_programma_in_memoria('./programma.txt', memoria)
  dscii = inizializza_dscii()

  # while program_counter >= 0:
  #  program_counter, registers, memory = execute_instruction(program_counter, registers, memory)

  print()

avvia_simulazione()