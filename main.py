import requests

for i in range(100):
    url = f"https://networking-ecommerce-new.onrender.com/profile?id={i}"
    r = requests.get(url=url)
    if r.status_code == 200:
        print(url)