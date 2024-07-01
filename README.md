# User Management API using Flask and MongoDB 
This API provides a comprehensive set of endpoints tailored to handle all the required tasks mentioned in the assignment description.

## Required packages
```python
pip install -r requirements.txt
```
## API Endpoints
1. **/users** - *GET* To fetch all the user names and email ids.
2. **/users/\<id\>** - *GET* To fetch specific user using unique User Id which is generate while user creation
3. **/users** - *POST* To create a new user with given data
4. **/users/\<id\>** - *PUT* To update users with the specified ID with new data.
5. **/users/\<id\>** - *DELETE* To delete the User with specified ID.

## API Endpoints
To create and run docker image, make sure docker engire is up and running

Open Command prompt and navigate to the working directory which has all the required files and excute the below commands.

```docker
docker-compose build
docker-compose up
```

## Testing in Postman
For testing in Postman API, use the same api url and change the JSON payload with respect to API endpoint.


*JSON Payload for Fetch Note*
```
{
    "email": "kitch1@gmail.com",
    "password": "9876543210",
    "name": "kishuu"
}
```
*Output from Server*
```
{
    "message": "User Id created successfully",
    "userId": "39a6b4c059a37c91"
}
```
