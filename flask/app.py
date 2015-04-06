import os
# Using Flask since Python doesn't have built-in session management
from flask import Flask, make_response, request, session, render_template, send_from_directory, redirect 
from werkzeug import secure_filename
import json
TREE_BASE_FILENAME = 'flare.json'
DATA_DIR = 'data'
DATA_DIR_PATH = '../{}'.format(DATA_DIR)
TREE_FILENAME = '{}/{}'.format(DATA_DIR_PATH, TREE_BASE_FILENAME)
ALLOWED_EXTENSIONS = set(['json'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

app = Flask(__name__, static_url_path='')
app.config.update(
    DEBUG=True,
    UPLOAD_FOLDER=DATA_DIR_PATH, 
)

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

@app.route('/tree/file', methods=['GET', 'POST'])
def download_tree_file():
    if request.method == 'POST':
        file = request.files['flare.json']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], TREE_FILENAME))
            return redirect('/web/index.html')
    else:
       with open(TREE_FILENAME, 'r') as tree_file:
               content = tree_file.read()
       response = make_response(content)
       response.headers["Content-Type"] = "application/json"
       response.headers["Content-Disposition"] = "attachment; filename={}".format(TREE_BASE_FILENAME)
       return response


@app.route('/web/<path:path>')
def send_web(path):
       return send_from_directory('..', path)

# Define a route for the webserver
@app.route('/')
def index():
       return redirect('/web/index.html')

if __name__ == '__main__':
	app.run( 
		host="0.0.0.0",
		port=int("8001")
	)

