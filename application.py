from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    """basic landing page."""
    return """<h1> Elastic Beanstalk CD</h1>"""


@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)