import secrets, string 

class Password_Generator():
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

    # Password with Constraints
    # while True: 
    #     for i in range(password_length):
    #         password += ''.join(secrets.choice(alphabet))

    #     if (any(char in special_characters for char in password) and sum(char in numbers for char in password) >=2 ): break

    print(password)