from flask import Flask
from flask_restful import Api
import api_endpoints

app = Flask(__name__)
api = Api(app)

# sanity check
@app.get("/")
def index():
    return "Working"

api.add_resource(api_endpoints.UsersData, '/users')
api.add_resource(api_endpoints.User, '/users/<string:id>')


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port= 5000, debug=True)