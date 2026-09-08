import requests

respons = requests.get("https://api.github.com/users/Sumptu")
data = respons.json()


nama = "Naren"
print(f"Halo, {nama}")
print(f"Repo Publik : {data['public_repos']}")
print(f"Tanggal Lahir Akun : {data['created_at']}")
