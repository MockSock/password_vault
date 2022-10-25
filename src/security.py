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
    
    # Find a way to make the next few sections methods 
    # Open and use key 
    with open('user.key', 'rb') as filekey:
        cypher = filekey.read()

    # Open file to encrypt
    with open('user_pwd.csv', 'rb') as file:
        original = file.read()

    # Encrypt file 
    encrypted = cypher.encrypt(original)

    # Write password to file 
    def savePwd(storagePwd):
        with open('user_pwd.csv', 'wb') as encrypted_file:
            encrypted_file.write(storagePwd) 

class Decryption:
