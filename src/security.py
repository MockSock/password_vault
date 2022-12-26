# this file will handle encryption, decryption, and tokenization

from cryptography.fernet import Fernet

class Security:
    # We use user file to be able to 
    # distinguish different users 

    def create_fileKey(self):
       fileKey = Fernet.generate_key() 
       return fileKey

    def write_fileKey(self, fileKey, user_file):
        with open(user_file, 'wb') as userFileKey:
            userFileKey.write(fileKey) 

    # Open and use key 
    def load_key(self, user_file):
        with open(user_file, 'rb') as userFilekey:
            userKey = userFilekey.read()
        return userKey

    # Open file to encrypt
    def encrypt_file():
        with open('user_pwd.csv', 'rb') as file:
            original = file.read()

        # Encrypt Contents of File
        encrypted = userKey.encrypt(original)

        # Lastly, write what is needed 
        with open('user_pwd.csv', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
