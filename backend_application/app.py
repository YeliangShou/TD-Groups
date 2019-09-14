from flask import Flask, render_template, request
from flask_cors import CORS
import json
from groups import *

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
  test("yo")
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

  user = request.get_json()
  userId = user["userId"]
  groupId = user["groupId"]
  assign_to_group(userId, groupId)
  return "Assigning user to group"

# Registering a new group
@app.route('/group', methods=['POST'])
def create_group():
  print(request.get_json())
  group_json = request.get_json()
  group_name = group_json["groupName"]
  group_members = group_json["groupMembers"]

  create_new_group(group_name, group_members)
  return "Creating group"

# Creating group categories
@app.route('/group/category', methods=['POST'])
def group_category():
  category_json = request.get_json()
  group_name = category_json["groupName"]
  category_name = category_json["groupName"]

  create_category(group_name, category_name)
  return "Hey"


# Creating category transactions
@app.route('/group/category/transaction', methods=['POST', 'GET'])
def create_transaction():
  if request.method == 'POST':
    print(request.get_json())
    transaction_json = request.get_json()
    group_name = transaction_json["groupName"]
    category_name = transaction_json["category_name"]
    create_category_transaction(group_name, category_name)

    return "Create transaction"
  elif request.method == 'GET':
    group_id = request.args.get('groupId')
    get_group_transactions(group_id)
    return "Return all transactions in a group category"
  else:
    return "err"

@app.route('/group/category/transaction/<string:transaction_id>')
def get_transaction(transaction_id):
  return "get specific transaction"


if __name__ == '__main__':
  app.run(debug=True)
