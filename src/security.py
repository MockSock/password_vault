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
            user_key = userFilekey.read()
        return user_key

    # Used for initial file encryption
    def encrypt_file(self, user_key, original_file, encrypted_file):

        cypher = Fernet(user_key)

        with open(original_file, 'rb') as file:
            original = file.read()

        # Encrypt Contents of File
        encrypted = cypher.encrypt(original)

        # Lastly, write what is needed 
        with open(encrypted_file, 'wb') as file:
            file.write(encrypted)

    # Used for after initial encryption
    def decrypt_file(self, user_key, encrypted_file, decrypted_file):

        cypher = Fernet(user_key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted_content = cypher.decrypt(encrypted)

        with open (decrypted_file, 'wb') as file:
            file.write(decrypted_content)
