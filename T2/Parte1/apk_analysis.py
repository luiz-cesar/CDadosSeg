import sys
import os
import re
import json

directory = sys.argv[1]
entries = os.listdir(directory)

apps = {}
permissions = {}

# Leitura dos arquivos na pasta
for entry in entries:
  with open(os.path.join(directory, entry), "r") as file:
    for line in file.readlines():
      # Regex para encontrar permissoes
      match = re.search(r'<uses-permission android:name="android.permission.([^"]*)"/>', line)
      if match:
        permission = match.group(1)
        if permission in permissions:
          permissions[permission].append(entry)
        else:
          permissions[permission] = [entry]
        if entry in apps:
          apps[entry].append(permission)
        else:
          apps[entry] = [permission]


# Impressao das permissoes de cada apk
print("""
===================

Permissões por APK

===================
""")
for key in apps:
  print("%s: %s" % (key.replace("AndroidManifest_", "").replace(".xml", ""), json.dumps(apps[key])))


# Impressao das permissoes unicas
print("""
===================

Permissões únicas por APK

===================
""")
apps_with_unique = {}
for key in permissions:
  if len(permissions[key]) == 1:
    if permissions[key][0] in apps_with_unique:
      apps_with_unique[permissions[key][0]].append(key)
    else:
      apps_with_unique[permissions[key][0]] = [key]
for key in apps_with_unique:
  print("%s: %s" % (key.replace("AndroidManifest_", "").replace(".xml", ""), json.dumps(apps_with_unique[key])))


# Impressao das permissoes comuns
common_permissions = []
print("""
===================

Permissões comuns das APKs

===================
""")
for key in permissions:
  if len(permissions[key]) == len(entries):
    common_permissions.append(key)
print(json.dumps(common_permissions))