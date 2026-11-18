import json
from pathlib import Path

from flask import Flask, jsonify

app = Flask(__name__)

DATA_FILE = Path(__file__).with_name("data.json")


def load_data():
    with DATA_FILE.open(encoding="utf-8") as file:
        return json.load(file)


dummy_data = load_data()


@app.route("/")
def home():
    return jsonify(message="Welcome to the Flask API!", data=dummy_data)


@app.route("/api")
def api():
    return jsonify(message="This is the API endpoint.", data=dummy_data)


@app.route("/health")
def health():
    return jsonify(status="healthy", data=dummy_data)


@app.route("/api/message")
def message():
    return jsonify(message="Hello from the Flask API!", data=dummy_data)


if __name__ == "__main__":
    app.run(debug=True)
