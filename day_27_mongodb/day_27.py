from flask import Flask, render_template
import pymongo
import os
from bson.objectid import ObjectId # id object

MONGODB_URI = 'mongodb+srv://gabriellopezmdp:mypass543@30daysofpython.e8et8ca.mongodb.net/?retryWrites=true&w=majority&appName=30daysofpython'
client = pymongo.MongoClient(MONGODB_URI)


db = client.thirtydaysofpython
# Creating students collection and inserting a document

# db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})

students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
#for student in students:
    # db.students.insert_one(student)

student = db.students.find_one({'_id':ObjectId('5df68a23f106fe2d315bbc8c')})

print(client.list_database_names())
print(student)

students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0 means not include and 1 means include
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

