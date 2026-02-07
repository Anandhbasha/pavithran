# pip install flask

from flask import Flask,jsonify,request

app = Flask(__name__)

users = []

@app.route('/',methods=["GET"])
def home():
    if len(users)==0:
        return "No records"
    return jsonify(users),200

@app.route('/add',methods=["POST"])
def addUser():
    data = request.json
    users.append(data)
    return jsonify({
        "message":"User Added Successfully","users":users
    }),201

@app.route('/editUser/<string:userName>',methods=['PUT'])
def updateUser(userName):
    data = request.json
    for user in users:
        if user["userName"] ==userName:
            user['userAge'] = data.get("userAge",user['userAge'])
            user['userAddress'] = data.get("userAddress",user['userAddress'])
        return jsonify({
        "message":"User Updated Successfully","users":users
    }),201


@app.route('/deleteUser/<string:userName>',methods=['DELETE'])
def delUser(userName):
    for user in users:
        if user["userName"] ==userName:
            users.remove(user)
        return jsonify({
        "message":"User Deleted Sucessfully Successfully"
    }),404
if __name__ =="__main__":
    app.run(debug=True)