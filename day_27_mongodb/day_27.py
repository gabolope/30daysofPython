from flask import Flask, render_template
import pymongo
import os

MONGODB_URI = 'mongodb+srv://gabriellopezmdp:mypass543@30daysofpython.e8et8ca.mongodb.net/?retryWrites=true&w=majority&appName=30daysofpython'
client = pymongo.MongoClient(MONGODB_URI)


db = client.thirtydaysofpython
# Creating students collection and inserting a document
db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

