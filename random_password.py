import secrets, string 

# All characters

letters = string.ascii_letters
numbers = string.digits
special_characters = string.punctuation

# Connect the characters together 
alphabet = letters + numbers + special_characters 

# Set a password length 
password_length = 18

# Now to generate the password
password = ''

for i in range(password_length): 
    password += ''.join(secrets.choice(alphabet))

print(password)