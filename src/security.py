# this file will handle encryption, decryption, and tokenization

from cryptography.fernet import Fernet

from random_password import password

# get password from user 
storagePwd = password
# for now it'll be randomly generated
fileKey = Fernet.generate_key()
fernet = Fernet(fileKey)

# Attack key to file for storage 
# Most likely will make a dictionary for a user that will have multiple passwords and sites
def saveFileKey():
    with open('user.key', 'wb') as filekey:
        filekey.write(fileKey)

# Open and use key 