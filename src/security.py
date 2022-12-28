# this file will handle encryption, decryption, and tokenization

from cryptography.fernet import Fernet

class Security():
    # We use user file to be able to 
    # distinguish different users 

    def create_file_key(self):
       file_key = Fernet.generate_key() 
       return file_key

    def write_file_key(self, file_key, user_file):
        with open(user_file, 'wb') as userfile_key:
            userfile_key.write(file_key) 

    # Open and use key 
    def load_key(self, user_file):
        with open(user_file, 'rb') as userfile_key:
            user_key = userfile_key.read()
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
