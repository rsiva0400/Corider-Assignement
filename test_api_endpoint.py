import pytest
import requests

api_url="http://127.0.0.1:5000"
valid_userId = '' # please paste a valid user id after creating a sample user

@pytest.mark.parametrize( "name, email, password, expected_status_code", [
        (None, 903, "pass123", 400),
        ('name', 'sample@gmail.com', "pass123", 200),
        ('name', 'sample@gmail.com', "pass123", 400),
    ] 
)

def test_createUser(name, email, password, expected_status_code):
    payload = {'name': name, 'email': email, 'password': password}
    response = requests.post(api_url + '/users', json=payload)

    assert response.status_code == expected_status_code

@pytest.mark.parametrize('id, expected_status_code',[
        ("invalid user id", 400),
        (valid_userId, 200)
    ]
)
def test_fetchUser(id, expected_status_code):
    response = requests.get(f"{api_url}/users/{id}")

    assert response.status_code == expected_status_code


if __name__ == "__main__":
    pytest.main()