# Current Goals: 
# Find a way to make a better constraint for the password maker
# Link up the security portion to api calls or connsole commands
# link site to password to sort them better 

from flask import Flask, render_template

from random_password import password
from security import Security

app = Flask(__name__)

@app.route('/')
def test_call():
    return render_template('index.html')
    
# Will create a random password
@app.route('/createpwd')
def create_pwd():
    return password

# Will read password from file 
@app.route('/findpwd')
def find_pwd():
    return Decryption.decryptedContent

if __name__ == '__main__':
    app.run()