# this file will handle encryption, decryption, and tokenization

from cryptography.fernet import Fernet

fileKey = Fernet.generate_key()
cypher = Fernet(fileKey)

class Encrytion:

    # Attack key to file for storage 
    # Most likely will make a dictionary for a user that will have multiple passwords and sites
    def saveFileKey():
        with open('user.key', 'wb') as filekey:
            filekey.write(fileKey)

    # Encrypt file 
    token = cypher.encrypt(original)

    # Write password to file 
    def savePwd(storagePwd):
        with open('user.key', 'wb') as encrypted_file:
            encrypted_file.write(storagePwd) 

class Decryption:

    # Open and use key 
    def useFileKey():
        with open('user.key', 'rb') as file:
            original = file.read()