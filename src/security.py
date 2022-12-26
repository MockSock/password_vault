# this file will handle encryption, decryption, and tokenization

from cryptography.fernet import Fernet

fileKey = Fernet.generate_key()

cypher = Fernet(fileKey)

class Security:

    def create_fileKey():
        with open('user.key', 'wb') as userFileKey:
            userFileKey.write(fileKey) 

    # Open and use key 
    def read_pwd():
        with open('user.key', 'rb') as userFilekey:
            cypher = userFilekey.read()
        return cypher

    # Open file to encrypt
    def encrypt_file():
        with open('user_pwd.csv', 'rb') as file:
            original = file.read()

        # Encrypt Contents of File
        encrypted = cypher.encrypt(original)

        # Lastly, write what is needed 
        with open('user_pwd.csv', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
