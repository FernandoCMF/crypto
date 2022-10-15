from telnetlib import ENCRYPT
from cryptography.fernet import Fernet

###### Gerando uma chave e gravando ele em um arquivo

#  key = Fernet.generate_key()

#  with open('filekey.key', 'wb') as filekey:
#     filekey.write(key)

# filekey.key = qFostZglB_ZyHbxhWKbxVzJe_Qt67XLRP8w7ulA_Zr4=

##### Criptografando a mensagem #####

with open('filekey.key', 'rb') as filekey:
   key = filekey.read()

fernet = Fernet(key)

with open('teste.txt', 'rb') as fileTest:
   content = fileTest.read()

encrypted = fernet.encrypt(content)

with open('teste.txt', 'wb') as fileTest_encrypted:
   fileTest_encrypted.write(encrypted)