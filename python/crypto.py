from cryptography.fernet import Fernet

##### Criptografando a mensagem #####

with open('filekey.key', 'rb') as filekey:
   key = filekey.read()

fernet = Fernet(key)

with open('teste.txt', 'rb') as fileTest:
   content = fileTest.read()

encrypted = fernet.encrypt(content)

with open('teste.txt', 'wb') as fileTest_encrypted:
   fileTest_encrypted.write(encrypted)