from flask import Blueprint, request
from src.app import User, db
from http import HTTPStatus 

app = Blueprint("user", __name__, url_prefix="/users")

def _create_user():
    data = request.json
    user = User(username=data["username"])
    db.session.add(user)
    db.session.commit()

@app.route("/", methods=["GET", "POST"])
def gandle_user():
    if request.method == "POST":
        _create_user()
        return {"message": "User created!"}, HTTPStatus.CREATED
    else:
        pass