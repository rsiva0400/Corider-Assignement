from flask import Flask, request, jsonify
import databaseFuntions as dbfunc


app = Flask(__name__)

# sanity check
@app.get("/")
def index():
    return "Working"

# Return all entries
@app.get("/users")
def fetchAllUsers():
    userlist = dbfunc.fetchAllUsers()
    return jsonify(userlist)

# fetch user by Id
@app.get('/users/<string:id>')
def fetchUserById(id):
    userData = dbfunc.fetchUserById(id)
    if userData:
        return jsonify(userData)
    else:
        return "User Id does not exit", 400

# create user 
@app.post("/users")
def createUser():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    # check for null values
    if not all(isinstance(var, str) for var in [name, email, password]):
        return "Invalid Values. Check the input.", 400
    
    # check whether email already exists
    if dbfunc.isEmailExist(email):
        return "Email already exists. Try new Email", 400
    
    userId = dbfunc.createUser(name, email, password)
    
    return jsonify({'message':'User Id created successfully', 'userId':userId})

# Updating user data
@app.put("/users/<string:id>")
def updateUser(id):

    if dbfunc.fetchUserById(id) is None:
        return "User Id does not exit", 400
    
    data = request.get_json()

    for field, value in data.items():
        dbfunc.updateUser(id, field, value)
    
    return "Updated Successfully"

# delete user
@app.delete("/users/<string:id>")
def deleteUser(id):

    # Check user Id
    if dbfunc.fetchUserById(id) is None:
        return "User Id does not exit", 400
    
    dbfunc.deleteUserById(id)

    return "User deleted successfully"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port= 5000, debug=True)