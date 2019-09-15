from flask import Flask, render_template, request, flash, redirect, url_for
from flask_jsglue import JSGlue
from flask_cors import CORS
from forms import GroupForm
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pyrebase
import requests

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
jsglue = JSGlue(app)
app.config['SECRET_KEY'] = '23d6332424c296c2bb6d2f1c4454fae2'
CORS(app)


@app.route('/')
def index():
  return render_template("home.html")

@app.route('/home')
def home():

  return render_template("home.html")

@app.route('/dashboard/<string:uid>/', methods=['GET', 'POST'])
def dashboard(uid):
  # Call the firebase database and get all the user info
  # user_doc = db.collection(u'users').document(uid).get().to_dict()
  # url = "https://api.td-davinci.com/api/customers/" + user_doc["td-customer-id"] + "/transactions"
  # headers = {"accept": 'application/json', "Authorization": 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiM2IyZDVhMTYtYTMwMC0zY2U2LTgzZTYtOTE2OWU4OTEzYzQ1IiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiI5MjVhZjU4Yi1kMmQzLTQ0MjctOGE2Zi1kM2Y1MGZjOGJlOTMifQ.RRdnWTXL8jMdlgKKQ_zAtazf78cF45FchafL4TlEA0g'}

  # print(requests.get(url, headers=headers).json())
  # transactions = (requests.get(url, headers=headers).json())["result"]
  # groups = []
  
  # for doc in db.collection("groups").get():
  #   if (doc.id in user_doc["groups"]): 
  #     groups.append(doc)
      
  # result = {"user": user_doc, "transactions": transactions[:10], "groups" : groups}


  form = GroupForm()
  if form.validate_on_submit():
    # form is an object with its fields
    flash("GOOD!")
    form = GroupForm()
    return redirect(url_for('dashboard', uid=uid))
  
  # print(result)
  result = ""
  return render_template("dashboard.html", user=result, form=form)
  
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
@app.route('/group', methods=['GET', 'POST'])
def create_group():
  # print(request.get_json())
  # group_json = request.get_json()
  # group_name = group_json["groupName"]
  # group_members = group_json["groupMembers"]

  # data = create_new_group(group_name, group_members)
  # db.collection(u'groups').document(u'').set(data)
  return render_template("group.html", user='user')

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
