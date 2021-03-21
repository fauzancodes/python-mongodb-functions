import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

database = input("Input Database Name: ")
collection = input("Input Collection Name: ")

mydb = myclient[database]
mycol = mydb[collection]

print("\n")

name = input("Input Website Name: ")
address = input("Input Website Address: ")
username = input("Input Username: ")
password = input("Input Password: ")

mylist = [
  { "name":name, "address":address, "username":username, "password":password}
]

mycol.insert_many(mylist)

print("\n")

continuing = input("Input Another Document? (y/n): ")

while continuing == "y" :
  print("\n")
  
  name = input("Input Website Name: ")
  address = input("Input Website Address: ")
  username = input("Input Username: ")
  password = input("Input Password: ")

  mylist = [
    { "name":name, "address":address, "username":username, "password":password}
  ]

  mycol.insert_many(mylist)

  print("\n")
  
  continuing = input("Input Another Document? (y/n): ")
else :
  print("Thank You")
