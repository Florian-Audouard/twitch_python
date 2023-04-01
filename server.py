import os
from flask import Flask, jsonify, render_template, request


os.chdir(os.path.dirname(__file__))


app = Flask(__name__)

# test


@app.route("/")
def index():  # pylint: disable=missing-function-docstring
    return render_template("index.html")


@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    return (
        jsonify(
            {"ip": request.remote_addr, "port": request.environ.get("REMOTE_PORT")}
        ),
        200,
    )


@app.route("/getDatabase", methods=["GET"])
def get_database():  # pylint: disable=missing-function-docstring
    return


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
