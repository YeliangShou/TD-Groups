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

  return render_template("home.html")

@app.route('/dashboard')
def dashboard():
  # Call the firebase database and get all the user info
  user = "Andrew"
  return render_template("dashboard.html", user=user)

# For registering a user
@app.route('/user', methods=['POST'])
def create_user():
  print(request.get_json())
  return "got user"

# Assigning a user to a new group
@app.route('/user/group', methods=['POST'])
def assign_user_to_group():
  print(request.get_json())
  return "Assigning user to group"

# Registering a new group
@app.route('/group', methods=['POST'])
def create_group():
  print(request.get_json())
  return "Creating group"

# Creating group categories
@app.route('/group/category', methods=['POST'])
def group_category():
  pass


if __name__ == '__main__':
  app.run(debug=True)
