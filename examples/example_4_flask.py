# ! pip install flask

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    """Return JSON response."""
    return jsonify({'status': 'ok', 'greetings': 'Hello World!'})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
