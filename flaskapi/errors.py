from flask import jsonify
from flaskapi import app

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error':'Not Data found'}), 404

@app.errorhandler(405)
def not_found(e):
    return jsonify({'error':'Method Not Allowed'}), 405

@app.errorhandler(400)
def not_found(e):
    return jsonify({'error':'Bad request'}), 400
