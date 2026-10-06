def leggi_programma_in_memoria (nome_file, memoria):
  with open(nome_file, 'r') as file_programma:
    contenuto = file_programma.read()
    lista_contenuto = contenuto.split('\n')
    if len(lista_contenuto) <= len(memoria):
      for i in range(len(lista_contenuto)):
        memoria[i] = int(lista_contenuto[i])
  return memoria