import secrets, string 

class Password_Generator:
    def generate_pwd(self):
        # All characters
        lower_case_letters = string.ascii_lowercase
        upper_case_letters = string.ascii_uppercase
        numbers = string.digits
        special_characters = string.punctuation

        # Connect the characters together 
        alphabet = lower_case_letters + upper_case_letters + numbers + special_characters 
        password_length = 18

        generated_password = ''.join(secrets.choice(alphabet) for x in range(password_length))

        print(generated_password)

        # no way to test if this generates a real password
        # for i in range(password_length): 
        #     generated_password += ''.join(secrets.choice(alphabet))
        
        # password = generated_password

        # return password
        

    # Password with Constraints
    # while True: 
    #     for i in range(password_length):
    #         password += ''.join(secrets.choice(alphabet))

    #     if (any(char in special_characters for char in password) and sum(char in numbers for char in password) >=2 ): break