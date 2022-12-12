# Current Goals: 
# Find a way to encrypt sensitive files
# Find a way to make a better constraint for the password maker
# Link up the security portion to api calls

from flask import Flask, render_template

from random_password import password

app = Flask(__name__)

@app.route('/')
def test_call():
    return render_template('index.html')
    
# Will create a random password
@app.route('/createpwd')
def create_pwd():
    return password

if __name__ == '__main__':
    app.run()