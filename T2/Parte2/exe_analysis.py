import pefile
import sys
import os
import json

def locate_data_sections(pe):
  data_sections = []
  for section in pe.sections:
    if section.Name == b'.text\x00\x00\x00':
      data_sections.append({
        'name': section.Name,
        'virtual_address': hex(section.VirtualAddress),
        'virtual_size': hex(section.Misc_VirtualSize),
        'size': section.SizeOfRawData,
      })
  return data_sections

directory = sys.argv[1]

output = {}
try:
  entries = os.listdir(directory)
  for entry in entries:
    pe = pefile.PE(os.path.join(directory, entry))
    output[entry] = locate_data_sections(pe)
except:
  pe = pefile.PE(sys.argv[1])
  output[sys.argv[1]] = locate_data_sections(pe)

print(output)

