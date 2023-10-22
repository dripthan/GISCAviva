
# imports
import sys
import pyperclip

# variables
assem = []
lines = []
states = {}

# instructions
insts = [
  'nop',
  'hlt',
  'lia',
  'lib',
  'lda',
  'ldb',
  'sta',
  'stb',
  'lap',
  'sap',
  'clr',
  'drw',
  'inp',
  'inc',
  'dec',
  'mic',
  'mdc',
  'add',
  'sub',
  'mul',
  'div',
  'shl',
  'shr',
  'not',
  'and',
  'or',
  'nnd',
  'nor',
  'xor',
  'cmp',
  'jmp',
  'jeq'
]

# loop through file and get src lines
with open(sys.argv[1]) as f:
  lines = f.readlines()
  lines = [line for line in lines if len(line.split()) > 0]
  lines = [line for line in lines if line.split()[0] != ';']

# loop through file and fill assem code with zeros
for line in lines:
  assem.append(hex(0))

# loop through file and get jump locations
for i, v in enumerate(lines):
  tokens = v.split()
  inst = tokens[0]
  if inst[-1] == ':':
    state = inst[0:-1]
    states[state] = i

# loop through file and deal with all insts
for i, v in enumerate(lines):
  tokens = v.split()
  inst = tokens[0]
  
  # skip state locations
  if inst[-1] == ':':
    continue

  inst_code = insts.index(inst)

  # deal with branching commands
  if inst in ['jmp', 'jeq']:
    param = states[tokens[1]]
    assem[i] = hex((inst_code << 8) + param)
    continue

  # deal with other commands
  param = 0
  if len(tokens) > 1:
    param = int(tokens[1], base=16)
  assem[i] = hex((inst_code << 8) + param)

pyperclip.copy(' '.join(assem))
print('paste it somewhere dawg')