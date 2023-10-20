#!/usr/bin/python3
'''
starts a Flask web application
'''


from flask import Flask, render_template

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    ''' display a HTML page only if n is an integer '''
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    ''' display a HTML page only if n is an integer '''
    if n % 2 == 0:
        res = "even"
    else:
        result = "odd"
        return result
    return render_template('6-number_odd_or_even.html', num=n, res=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
