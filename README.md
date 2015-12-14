# disasm
Disassemble helper using darm (https://github.com/jbremer/darm)

# HowTo
cp disasm.py into the darm directory

  1. $ python dis.py
  --> Disassemble from your input until ctrl + c
  2. $ python dis.py e5900004 e7d3001f ...
  --> Disassemble from serialized input (2 or more)
  3. $ python dis.py ~/op.txt
  --> Disasemble from a file

file same (op.txt)
```c
e586d000 
e59f5068 
e59fc068
```
