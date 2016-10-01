import requests

def register(token, github):
    token = "ea2915199244159af63987b64d1957c5"
    auth = {"github": "https://github.com/Joshlix95/CODE2040-APP-2017", "token":token}
    r = requests.post("http://challenge.code2040.org/api/register", json = auth)
    
    return r


