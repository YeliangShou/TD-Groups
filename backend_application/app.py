from flask import Flask, render_template, request
from flask_cors import CORS
from forms import GroupForm
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pyrebase

import json
from groups import *

# Use the application default credentials
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': u"td-groups",
})

db = firestore.client()

config = {
  "apiKey": "AIzaSyBST-3U14ztUoOfIADZ00hfl3vFlW-TN8Q",
  "authDomain": "td-groups.firebaseapp.com",
  "databaseURL": "https://td-groups.firebaseio.com/",
  "storageBucket": "td-groups.appspot.com"
}

firebase = pyrebase.initialize_app(config)
app = Flask(__name__)
app.config['SECRET_KEY'] = '23d6332424c296c2bb6d2f1c4454fae2'
CORS(app)


@app.route('/')
def index():
  return render_template("home.html")

@app.route('/home')
def home():

  return render_template("home.html")

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
  # Call the firebase database and get all the user info

  user = "test-user"

  users_ref = db.collection(u'users')
  docs = users_ref.stream()

  for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))

  form = GroupForm()

  return render_template("dashboard.html", user=user, form=form)

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

  data = create_new_group(group_name, group_members)
  db.collection(u'groups').document(u'').set(data)
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

@app.route('/group/category/<string:category_id>/transaction/<string:transaction_id>')
def get_transaction(category_id, transaction_id):
  get_single_transaction(category_id, transaction_id)
  return "get specific transaction"


if __name__ == '__main__':
  app.run(debug=True)
