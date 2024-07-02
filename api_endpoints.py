from flask_restful import Resource
import databaseFuntions as dbfunc
from flask import jsonify, request

class UsersData(Resource):

    ''' Resource Class to perform operation on UserDatabase'''

    def get(self):
        ''' API Endpoint to fetch all users'''
        userlist = dbfunc.fetchAllUsers()
        return jsonify(userlist)
    
        
    def post(self):
        '''Creates a new user with the specified data.'''
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

    
    
class User(Resource):

    ''' Resource Class to perform operation on user with Specified ID'''
    
    def get(self,id):
        ''' API Endpoint to fetch user with specified ID'''
        userData = dbfunc.fetchUserById(id)
        if userData:
            return jsonify(userData)
        else:
            return "User Id does not exit", 400
        
    def put(self,id):
        '''Updates the user with the specified ID with the new data'''
        if dbfunc.fetchUserById(id) is None:
            return "User Id does not exit", 400
        
        data = request.get_json()

        for field, value in data.items():
            dbfunc.updateUser(id, field, value)
        
        return "Updated Successfully"
    
    def delete(self,id):
        '''Deletes the user with the specified ID.'''

        # Check user Id
        if dbfunc.fetchUserById(id) is None:
            return "User Id does not exit", 400
        
        dbfunc.deleteUserById(id)

        return "User deleted successfully"