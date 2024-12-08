import requests

uri = "http://localhost:5049/api"


def login(username: str, password: str):
    resp = requests.post(uri + "/login", data=f"username={username}&password={password}", headers={"Content-Type": "application/x-www-form-urlencoded"})
    assert resp.status_code == 200, resp.text

    print("Login OK")
    return resp.json()["access_token"]


def test_unauthorized_get_secret():
    resp = requests.get(uri + "/secret")
    assert resp.status_code == 401, resp.text

    print("Unauthorized secret OK")


def test_authorized_get_secret(token: str):
    resp = requests.get(uri + "/secret", headers={"Authorization": "Bearer " + token})
    assert resp.status_code == 200, resp.text
    assert resp.json() == {"secret_data": "This is top secret information!"}

    print("Authorized secret OK")


if __name__ == "__main__":
    test_unauthorized_get_secret()
    token = login("user@example.com", "string")
    test_authorized_get_secret(token)
