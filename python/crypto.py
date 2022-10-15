from cryptography.fernet import Fernet

###### Gerando uma chave e gravando ele em um arquivo

key = Fernet.generate_key()

with open('filekey.key', 'wb') as filekey:
   filekey.write(key)



