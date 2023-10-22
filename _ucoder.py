
# imports
import pyperclip

# all ucode
clr = 0b1000000000000000000000000000
drw = 0b0100000000000000000000000000
inp = 0b0010000000000000000000000000
ain = 0b0001000000000000000000000000
bIn = 0b0000100000000000000000000000
cin = 0b0000010000000000000000000000
din = 0b0000001000000000000000000000
aou = 0b0000000100000000000000000000
bou = 0b0000000010000000000000000000
cou = 0b0000000001000000000000000000
dou = 0b0000000000100000000000000000
mai = 0b0000000000010000000000000000
iri = 0b0000000000001000000000000000
fgi = 0b0000000000000100000000000000
zeo = 0b0000000000000010000000000000
uno = 0b0000000000000001000000000000
pci = 0b0000000000000000100000000000
pco = 0b0000000000000000010000000000
pce = 0b0000000000000000001000000000
end = 0b0000000000000000000100000000
op3 = 0b0000000000000000000010000000
op2 = 0b0000000000000000000001000000
op1 = 0b0000000000000000000000100000
op0 = 0b0000000000000000000000010000
alo = 0b0000000000000000000000001000
rin = 0b0000000000000000000000000100
r1o = 0b0000000000000000000000000010
r0o = 0b0000000000000000000000000001

# fetch cycle
fetch = [ pco | mai, r1o | iri | pce ]

# arrays
ucode = []
insts = [

  fetch + [ end ],
  [  ],

  fetch + [ r0o | ain, end ],
  fetch + [ r0o | bIn, end ],

  fetch + [ r0o | mai, r0o | ain, end ],
  fetch + [ r0o | mai, r0o | bIn, end ],

  fetch + [ r0o | mai, aou | rin, end ],
  fetch + [ r0o | mai, bou | rin, end ],

  fetch + [ bou | mai, r0o | ain, end ],
  fetch + [ bou | mai, aou | rin, end ],

  fetch + [ clr, end ],
  fetch + [ drw, end ],
  fetch + [ inp | ain, end ],

  fetch + [ uno | bIn, alo | ain, end ],
  fetch + [ uno | bIn, alo | ain | op0, end ],

  fetch + [ r0o | mai, r0o | ain, uno | bIn, alo | ain, aou | rin, end ],
  fetch + [ r0o | mai, r0o | ain, uno | bIn, alo | op0 | ain, aou | rin, end ],

  fetch + [ alo | ain | 0x0 | 0x0 | 0x0 | 0x0 | fgi, end ],
  fetch + [ alo | ain | 0x0 | 0x0 | 0x0 | op0 | fgi, end ],
  fetch + [ alo | ain | 0x0 | 0x0 | op1 | 0x0 | fgi, end ],
  fetch + [ alo | ain | 0x0 | 0x0 | op1 | op0 | fgi, end ],
  fetch + [ alo | ain | 0x0 | op2 | 0x0 | 0x0 | fgi, end ],
  fetch + [ alo | ain | 0x0 | op2 | 0x0 | op0 | fgi, end ],

  fetch + [ alo | ain | 0x0 | op2 | op1 | 0x0 | fgi, end ],
  fetch + [ alo | ain | 0x0 | op2 | op1 | op0 | fgi, end ],
  fetch + [ alo | ain | op3 | 0x0 | 0x0 | 0x0 | fgi, end ],
  fetch + [ alo | ain | op3 | 0x0 | 0x0 | op0 | fgi, end ],
  fetch + [ alo | ain | op3 | 0x0 | op1 | 0x0 | fgi, end ],
  fetch + [ alo | ain | op3 | 0x0 | op1 | op0 | fgi, end ],
  fetch + [ fgi, end],

  fetch + [ r0o | pci, end ],
  fetch + [ end ]

]

# allocate ucode memory
for flag in range(2):
  for inst in range(0b11111 + 1):
    for step in range(0b1111 + 1):
      ucode.append(hex(0))

# generate ucode
for flag in range(2):
  for inst in range(0b11111 + 1):
    for step in range(0b1111 + 1):
      ucode_index = (flag << 9) + (inst << 4) + step
      if inst < len(insts):
        current_inst = insts[inst]
        # check to see if jump
        if inst == 0x1f and flag == 1:
          current_inst = fetch + [ r0o | pci, end ]
        if step < len(current_inst):
          ucode[ucode_index] = hex(current_inst[step])

# copy ucode to clipboard
pyperclip.copy(' '.join(ucode))
print('paste it somewhere dawg')