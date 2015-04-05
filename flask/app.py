import os
# Using Flask since Python doesn't have built-in session management
from flask import Flask, request, session, render_template, send_from_directory
import json
TREE_FILENAME = '../flare.json'

app = Flask(__name__, static_url_path='')

# Generate a secret random key for the session
app.secret_key = os.urandom(24)

@app.route('/tree', methods=['GET', 'POST'])
def tree():
    if request.method == 'POST':
       content = request.data
       with open(TREE_FILENAME, 'w') as tree_file:
           tree_file.write(content)
       return "saved."
    else:
       with open(TREE_FILENAME, 'r') as tree_file:
           content = tree_file.read()
       return content

@app.route('/web/<path:path>')
def send_web(path):
       return send_from_directory('..', path)

# Define a route for the webserver
@app.route('/')
def index():
       return send_from_directory('..', path)

if __name__ == '__main__':
	app.run( 
		host="0.0.0.0",
		port=int("8001")
	)

