from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/user/<string:name>/<int:years>")
def user_profile(name, years):
	return {'name':name, 'years':years,}
