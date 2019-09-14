from flask import Flask, render_template, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
  return 'Hello world'

@app.route('/home')
def home():
  return 'my home'

@app.route('/dashboard')
def dashboard():
  return "yeetboard"

# For registering a user
@app.route('/user', methods=['POST'])
def create_user():
  print(request.get_json())
  return "got user"

# Registering a new group
@app.route('/group', methods=['POST'])
def create_group():
  print(request.get_json())
  return "Creating group"

# Assigning a user to a new group
@app.route('/group', methods=['POST'])
def assign_user_to_group():
  print(request.get_json())
  return "Assigning user to group"


if __name__ == '__main__':
  app.run(debug=True)
