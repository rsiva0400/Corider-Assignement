from pymongo import MongoClient
import bcrypt
import secrets


MyClient = MongoClient("localhost",27017)

UserDB = MyClient.UserDataBase

UsersCol = UserDB.UsersCol

salt = bcrypt.gensalt()


def fetchAllUsers():
    result = UsersCol.find({}, {'_id':0, 'name': 1, 'email': 1})
    emailList, userList = [], []
    for i in result:
        emailList.append(i['email'])
        userList.append(i['name'])
    return {"names": userList, "emails": emailList}

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
        # generate a unique User Id
        userId = secrets.token_hex(8)

        # Hash the password before storing
        hashedPass = bcrypt.hashpw(password.encode('utf-8'), salt)
        result = UsersCol.insert_one({
            '_id': userId, 'name':name, 
            'password': hashedPass, 'email': email})
        
        # returning the user id
        return result.inserted_id
    
    # Generate new user id if the generated Id already exists
    except:
        createUser(name, email, password)

def updateUser(id, field, newData):
    UsersCol.find_one_and_update({"_id":id}, { "$set": { str(field) : newData } })
        
def deleteUserById(id):
    UsersCol.find_one_and_delete({ '_id': id })