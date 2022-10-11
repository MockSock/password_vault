# Current Goals: 
# Create a way to store and retrieve passwords
# Find a way to encrypt sensitive files
# Create a login for user 
# Find a way to make a better constraint for the password maker

import string
from flask import Flask, render_template

user = ''
# common acryonym for password
pwd = ''

app = Flask(__name__)

@app.route('/')
def test_call():
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run()