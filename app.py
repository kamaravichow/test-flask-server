from flask_cors import CORS
from flask import Flask, jsonify, request, render_template
import os
import json


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "status": 200,
        "message": "Health Ok",
    })


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
