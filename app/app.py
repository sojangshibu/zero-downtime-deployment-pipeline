from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "v1")


@app.route("/")
def home():
    return jsonify({
        "application": "zero-downtime-deployment",
        "version": APP_VERSION,
        "message": f"Running application {APP_VERSION}"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "version": APP_VERSION
    }), 200


@app.route("/error")
def error():
    return jsonify({
        "status": "error",
        "version": APP_VERSION
    }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
