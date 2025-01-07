from flask import Flask, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page"


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p"


@app.route("/user/<string:username>/<int:idade>/<float:peso>")
def show_user_profile(username, idade, peso):
    return f"Olá {username}, você tem {idade} e {peso} Kg"


# Converter types:
# string: (default) accepts any text without a slash
# int accepts positive integers
# float accepts positive floating point values
# path like string but also accepts slashes
# accepts UUID strings


@app.route("/projects/")
def projects():
    return "The projects page"


@app.route("/about")
def about():
    return "The about page"


# The canonical URL for the projects endpoint has a trailing slash.
# It's similar to a folder in a file ystem. If you access the URL without a trailing slash
# (/projects), Flask redirects you to the canonical URL with the trailing slash (/projects)

# The canonical URL for the about endpoint does not have a trailing slash.
# It’s similar to the pathname of a file. Accessing the URL with a trailing slash (/about/)
# produces a 404 “Not Found” error. This helps keep URLs unique for these resources,
# which helps search engines avoid indexing the same page twice.#

with app.test_request_context():
    print(url_for("index"))
    print(url_for("show_user_profile", username="Gabriel", idade=22, peso=74.60))
    print(url_for("hello_world"))
    print(url_for("projects"))
    print(url_for("about"))


@app.route("/methods", methods=["GET", "POST"])
def methods():
    if request.method == "POST":
        return "methods POST"
    else:
        return "methods GET"


# By default, a route only answears to GET request.
# You can saparete views for different methods into different functions

# @app.get('/login')
# @app.post('/login')

# You can also separe views
