#!/usr/bin/python3
'''
starts a Flask web application
'''


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    ''' display “Hello HBNB!” '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def horbolton():
    ''' display “HBNB” '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    ''' display “C” '''
    return 'C {}'.format(text.replace('_', " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    ''' display “Python” '''
    return 'Python {}'.format(text.replace('_', " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    ''' display “n” only if n is an integer '''
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
