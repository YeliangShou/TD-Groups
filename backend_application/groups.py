import requests

TD_API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJDQlAiLCJ0ZWFtX2lkIjoiODE1YTA1MTktMDg5Ny0zOWFlLWI1YWQtZThhZTE2ZDk5ZjRiIiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJhcHBfaWQiOiI5MjVhZjU4Yi1kMmQzLTQ0MjctOGE2Zi1kM2Y1MGZjOGJlOTMifQ._Y5yFZk-ZzAUKWA3dZ7xOxsXt2fV5taZ8tZb2_NmRmg'

def test(p):
  print("this is " + p)

def assign_to_group(userId, groupId):
  pass

def create_new_group(group_name, group_members):
  data = {"groupId": group_name,
          "members": [group_members],
          "categories": {}}
  return data

def create_category(group_name, category_name):
  pass

def get_group_transactions(group_id):
  pass

def create_category_transaction(group_name, category_name):
  pass

def get_single_transaction(category_id, transaction_id):
  pass

def get_all_user_transactions(user_id):
  response = requests.get(f'https://api.td-davinci.com/api/customers/{user_id}/transactions',
    headers = { 'Authorization': TD_API_KEY })
  