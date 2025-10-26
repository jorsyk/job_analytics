import requests

r = requests.get("https://api.hh.ru/vacancies?text=Python")
print(r.json())
