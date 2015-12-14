import os
import sys
import darm

opCount = len(sys.argv) - 1
opList = []
if opCount is 0 :
  print "Disassemble helper using darm"
  print "supports ARMv7/Thumb/Thumb2, VFP/Neon/SIMD upcoming..."
  print " Usage : python disasm.py <machine code ...>"
  print " 1. $ python disasm.py"
  print "  --> Disassemble from your input until ctrl + c"
  print " 2. $ python disasm.py e5900004 e7d3001f ..."
  print "  --> Disassemble from serialized input (2 or more)"
  print " 3. $ python disasm.py ~/op.txt"
  print "  --> Disasemble from a file"

  print "please input machine code: \n"
  while True :
    input_int = raw_input("")
    hexValue = int(input_int, 16)
    print str(darm.disasm_armv7(hexValue))
elif opCount is 1 :
  path = sys.argv[1]
  if os.path.exists(path) :
    print "Disassemble a file %s" % path
    filein = open(path, "r")
    lines = filein.readlines()

    for line in lines :
      print "%s\t%s" % (line.rstrip('\n'), str(darm.disasm_armv7(int(line, 16))))
  else :
    print "%s is not exist" % path
else :
  # print str(darm.disasm_armv7(0xe1a00002))
  for i in range(opCount) :
    opList.append(sys.argv[i+1])
  
  for opIndex in range(opCount) :
    try :
      print str(darm.disasm_armv7(int(opList[opIndex], 16)))
    except ValueError :
      pass
