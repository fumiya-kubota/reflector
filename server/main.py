from flask import Flask, render_template, jsonify
import os
import glob
import json


app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/api/models.json')
def resources():
    return jsonify(models=['a', 'b'])


if __name__ == "__main__":
    app.run(host='0.0.0.0')
