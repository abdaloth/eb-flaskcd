from flask import Flask
from flask import render_template

application = Flask(__name__)

@application.route('/')
def hello():
    """simple landing Page."""
    return render_template('hello_eb.html')

if __name__ == '__main__':
    application.run(host='127.0.0.1', port=8080, debug=True)