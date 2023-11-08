#!/usr/bin/python3
"""Your Flask Web Application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from uuid import UUID

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
    return render_template('7-states_list.html', states=state)


@app.route('/cities_by_states', strict_slashes=False)
def list_cities():
    """List all states and their cities"""
    state = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=state)


@app.route('/states', strict_slashes=False)
def states_list():
    """
    Route that displays a list of all State objects
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def _id(id):
    """Display a HTML page with a list of all State objects
    try:
        id_int = int(id)
        state = storage.get(State, id_int)
    except ValueError:
        try:
            id_uuid = UUID(id)
            state = storage.get(State, id_uuid)
        except ValueError:
            state = None

    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html')
    """
    try:
        # Try to parse the ID as an integer
        id_int = int(id)
        state = storage.get(State, id_int)
    except ValueError:
        # If parsing as an integer fails, try to parse as a UUID
        try:
            id_uuid = UUID(id)
            state = storage.get(State, id_uuid)
        except ValueError:
            # If both attempts fail, set state to None
            state = None

    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', states={state.id: state}, with_id=True)
    else:
        return render_template('9-states.html', not_found=True, states={})
@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
