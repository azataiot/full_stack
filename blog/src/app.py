import pymongo


# using mongodb
# start mongodb on te terminal by `mongod` and then
uri = "mongodb://127.0.0.1:27017/"
client = pymongo.MongoClient(uri) # init the database
database = client["fullstack"] # name of the database we use in this app
collection = database["students"] # use the database collections in the fullstack database
students = collection.find({})
#print(students) # not printing the right staff ,<pymongo.cursor.Cursor object at 0x104f4e470>
for student in students:
    print(student)