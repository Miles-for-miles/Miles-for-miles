# this code is for you to use in replit

from replit import db

# run following after one time and then switch "store" to "db["store"]"
store = 0
db["store"] = store

def update():
  global store
  store = db["store"]
  db["store"] = store
  store = db["store"]
  
# use update() to update "store"
