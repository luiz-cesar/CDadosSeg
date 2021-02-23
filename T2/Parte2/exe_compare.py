import pefile
import sys
import os
import json

file1 = sys.argv[1]
file2 = sys.argv[2]

pe1 = pefile.PE(file1)
pe2 = pefile.PE(file2)

print(pe1)