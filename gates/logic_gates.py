def not_gate (a):
  if a == 0:
    return 1
  else:
    return 0

def and_gate (a, b):
  if a == 1 and b == 1:
    return 1
  else:
    return 0

def nand_gate (a, b):
  return not_gate(and_gate(a, b))

def read_write_1_bit (data, write, d_flip_flop):
  d_flip_flop["out1"] = nand_gate(data, write)
  d_flip_flop["out2"] = nand_gate(d_flip_flop["out1"], write)
  if data == 1:
    d_flip_flop["out3"] = nand_gate(d_flip_flop["out1"], d_flip_flop["out4"])
    d_flip_flop["out4"] = nand_gate(d_flip_flop["out2"], d_flip_flop["out3"])
  else:
    d_flip_flop["out4"] = nand_gate(d_flip_flop["out2"], d_flip_flop["out3"])
    d_flip_flop["out3"] = nand_gate(d_flip_flop["out1"], d_flip_flop["out4"])

  return d_flip_flop["out3"]

def get_d_flip_flop ():
  d_flip_flop = {"out1": 0, "out2": 0, "out3": 0, "out4": 0}
  return d_flip_flop

def get_memory_cell ():
  flip_flops = []
  for _ in range(8):
    flip_flops.append(get_d_flip_flop())
  return flip_flops

def read_memory_cell (cell):
  res = 0
  exp = 0
  for i in range(len(cell) - 1, -1, -1):
    res += read_write_1_bit(0, 0, cell[i]) * (2 ** exp)
    exp += 1
  return res

def convert_to_binary (value):
  binary_digits = [0, 0, 0, 0, 0, 0, 0, 0]
  i = len(binary_digits) - 1
  while value > 0:
    remainder = value % 2
    binary_digits[i] = remainder
    value = value // 2
    i -= 1
  return binary_digits

def write_memory_cell (cell, value):
  binary_digits = convert_to_binary(value)
  for i in range(len(cell)):
    read_write_1_bit(binary_digits[i], 1, cell[i])

cell1 = get_memory_cell()
print(read_memory_cell(cell1))
write_memory_cell(cell1, 42)
print(read_memory_cell(cell1))
write_memory_cell(cell1, 43)
print(read_memory_cell(cell1))
print(read_memory_cell(cell1))