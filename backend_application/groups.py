
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