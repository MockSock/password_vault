# this file will handle encryption, decryption, and tokenization

from cryptography.fernet import Fernet

fileKey = Fernet.generate_key()
fernet = Fernet(fileKey)

# Attack key to file for storage 
# Most likely will make a dictionary for a user that will have multiple passwords and sites
def saveFileKey():
    with open('user.key', 'wb') as filekey:
        filekey.write(fileKey)

# Open and use key 
with open('user.key', 'rb') as file:
    original = file.read()

# Encrypt file 
encryptAction = fernet.encrypt(original)

# Write password to file 
def savePwd(storagePwd):
    with open('user_pwd.txt', 'wb') as encrypted_file:
        encrypted_file.write(storagePwd)