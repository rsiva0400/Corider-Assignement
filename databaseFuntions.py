from pymongo import MongoClient, errors
import bcrypt
import secrets

import os

mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/mydatabase')
MyClient = MongoClient(mongo_uri)

UserDB = MyClient.UserDataBase

UsersCol = UserDB.UsersCol

salt = bcrypt.gensalt()


def fetchAllUsers():
    result = UsersCol.find({})
    userIds, emailList, userList = [], [], []
    for i in result:
        emailList.append(i['email'])
        userList.append(i['name'])
        userIds.append(i['_id'])
    return {"names": userList, "emails": emailList, "userId": userIds}


def fetchUserById(id):
    result = UsersCol.find_one({'_id':id}, {'_id':0, 'name': 1, 'email' : 1})
    return result

def isEmailExist(email):
    result = UsersCol.find_one({'email':email})

    if result:
        return True
    else:
        return False


def createUser(name, email, password):
    try:
        userId = secrets.token_hex(8)

        hashedPass = bcrypt.hashpw(password.encode('utf-8'), salt)
        result = UsersCol.insert_one({
            '_id': userId, 'name':name, 
            'password': hashedPass, 'email': email})
        
        return result.inserted_id
    
    # Generate new user id if the generated Id already exists
    except errors.DuplicateKeyError:
        createUser(name, email, password)

def updateUser(id, field, newData):
    UsersCol.find_one_and_update({"_id":id}, { "$set": { str(field) : newData } })
        
def deleteUserById(id):
    UsersCol.find_one_and_delete({ '_id': id })