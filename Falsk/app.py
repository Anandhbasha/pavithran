# pip install flask

from flask import Flask,jsonify,request
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# mongodb connection
# pip install pymongo
client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["NewStudentBataBase"]
collection = db["NewDb"]
print("Db is Connect")

@app.route('/',methods=["GET"])
def getUsers():
    users = []
    for user in collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return jsonify(users)

@app.route('/add',methods=["POST"])
def addUser():
    data = request.json
    res = collection.insert_one(data)
    return jsonify({
        "message":"User Added Successfully","_id":str(res.inserted_id)
    }),201

@app.route('/editUser/<id>',methods=['PUT'])
def updateUser(id):
    data = request.json
    res = collection.update_one({
        "_id":ObjectId(id)
    },{"$set":data})
    if res.matched_count==0:
        return jsonify({"error":"User Not found"}),404
    return jsonify({
        "message":"User Updated Successfully"
    }),201


@app.route('/deleteUser/<id>',methods=['DELETE'])
def delUser(id):
    res = collection.delete_one({"_id":ObjectId(id)})
    if res.deleted_count==0:
        return jsonify({
            "error":"User Not found"
        }),404
    return jsonify({
        "message":"User Deleted Success fully"
    })

# read one
@app.route("/user/<id>",methods=["GET"])
def getUser(id):
    user = collection.find_one({"_id":ObjectId(id)})
    if not user:
        return jsonify({"error":"User Not found"}),404
    user["_id"]= str(user["_id"])
    return jsonify(user)
if __name__ =="__main__":
    app.run(debug=True)