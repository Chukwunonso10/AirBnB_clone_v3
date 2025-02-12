#!/usr/bin/python3
"""Begining of flask web application"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(error):
    """method to handle @app.teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """handler that returns a JSON-formatted 404 status code response"""
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(host=getenv('HBNB_API_HOST'),
            port=getenv('HBNB_API_PORT'),
            threaded=True)
