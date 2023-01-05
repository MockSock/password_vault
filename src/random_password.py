import secrets, string 

class Password_Generator:
    password = ''

    def generate_pwd(self, password):
        # All characters

        letters = string.ascii_letters
        numbers = string.digits
        special_characters = string.punctuation

        # Connect the characters together 
        alphabet = letters + numbers + special_characters 
        password_length = 18
        for i in range(password_length): 
            generated_password += ''.join(secrets.choice(alphabet))
        
        password = generated_password

        return password

    # Password with Constraints
    # while True: 
    #     for i in range(password_length):
    #         password += ''.join(secrets.choice(alphabet))

    #     if (any(char in special_characters for char in password) and sum(char in numbers for char in password) >=2 ): break