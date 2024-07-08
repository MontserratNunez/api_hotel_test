from flask import Flask, request, jsonify
import read_write

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def index():
    return ""


if __name__ == "__main__":
    app.run()