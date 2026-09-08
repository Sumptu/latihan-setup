import requests

respons = requests.get("https://api.github.com/users/Sumptu")
data = respons.json()


nama = "Naren"
print(f"Halo, {nama}")
print(f"{data['public_repos']}")
print(f"{data['created_at']}")
