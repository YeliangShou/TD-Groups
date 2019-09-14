from flask import Flask, render_template, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
  return 'Hello world'

if __name__ == '__main__':
  app.run(debug=True)