from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/api")
def api():
    return jsonify(message="This is the API endpoint.")

@app.route("/health")
def health():
    return jsonify(status="healthy")


@app.route("/api/message")
def message():
    return jsonify(message="Hello from the Flask API!")


if __name__ == "__main__":
    app.run(debug=True)
