import requests

respons = requests.get("https://api.github.com/users/Sumptu")
data = respons.json()


nama = "Naren"
print(f"Halo, {nama}")
print(data["public_repos"])
print(data["created_at"])
