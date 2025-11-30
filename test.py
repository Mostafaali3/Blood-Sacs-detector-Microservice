import requests

files = {"file": open("image.png", "rb")}

resp = requests.post("http://127.0.0.1:8000/caption", files=files)
print(resp.json())
