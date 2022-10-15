from cryptography.fernet import Fernet

with open('filekey.key', 'rb') as filekey:
   key = filekey.read()

fernet = Fernet(key)

with open('teste.txt', 'rb') as fileTest:
   content = fileTest.read()

decrypted = fernet.decrypt(content)

with open('teste.txt', 'wb') as fileTest_decrypted:
   fileTest_decrypted.write(decrypted)