import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

database = input("Input Database Name: ")
collection = input("Input Collection Name: ")

mydb = myclient[database]
mycol = mydb[collection]

print("\n")

inputColumn1 = input("Input Column1: ")
inputColumn2 = input("Input Column2: ")
inputColumn3 = input("Input Column3: ")
inputColumn4 = input("Input Column4: ")

mylist = [
  { "column1Name":inputColumn1, "column2Name":inputColumn2, "column3Name":inputColumn3, "column41Name":inputColumn4}
]

mycol.insert_many(mylist)

print("Document has been inserted")

print("\n")

continuing = input("Input Another Document? (y/n): ")

while continuing == "y" :
  print("\n")

  inputColumn1 = input("Input Column1: ")
  inputColumn2 = input("Input Column2: ")
  inputColumn3 = input("Input Column3: ")
  inputColumn4 = input("Input Column4: ")

  mylist = [
    { "column1Name":inputColumn1, "column2Name":inputColumn2, "column3Name":inputColumn3, "column41Name":inputColumn4}
  ]

  mycol.insert_many(mylist)
  
  print("Document has been inserted")

  print("\n")

  continuing = input("Input Another Document? (y/n): ")
else :
  print("Thank You")
