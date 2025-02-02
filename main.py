#!/usr/bin/python3
"""Write a script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0 , port 5000
    Routes:
        / : display “Hello HBNB!”
"""
from flask import *

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Hello HBNB! output for hello route /"""
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
