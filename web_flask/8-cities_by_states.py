#!/usr/bin/python3
"""Your Flask Web Application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

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
        result = "even"
    else:
        result = "odd"
    return render_template('6-number_odd_or_even.html', num=n, res=result)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """List all states and their cities"""
    state = sorted(storage.all(State).values(), key=lambda x: x.name)
    # city = storage.all(City).values()
    return render_template('7-states_list.html', states=state)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
