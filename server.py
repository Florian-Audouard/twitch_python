import os
from flask import Flask, jsonify, render_template, request
from database import reset_table, get_data, add_message
from flask_cors import CORS

os.chdir(os.path.dirname(__file__))


app = Flask(__name__)
CORS(app)


@app.route("/")
def index():  # pylint: disable=missing-function-docstring
    return render_template("index.html")


@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    save_ip = get_data()
    raw_ip = request.remote_addr
    ip = raw_ip + "-1"
    # count = 2
    # while ip in save_ip:
    #     ip = raw_ip + "-" + count
    #     count += 1

    return (
        jsonify({"ip": ip}),
        200,
    )


@app.route("/getDatabase", methods=["GET"])
def get_database():  # pylint: disable=missing-function-docstring
    return


@app.route("/reset", methods=["GET"])
def reset():  # pylint: disable=missing-function-docstring
    reset_table()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
