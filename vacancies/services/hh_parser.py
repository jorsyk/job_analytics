import requests

def parse_vacancies():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
        "Accept": "*/*"
    }
    response = requests.get(url="https://api.hh.ru/vacancies?text=Python разработчик", headers=headers)
    data = response.json()
    vacancies = data["items"]
    for vacancy in vacancies:
        print({
            "title": vacancy.get("name"),
            "company": vacancy.get("employer", {}).get("name"),
            "city": vacancy.get("area", {}).get("name"),
            "salary_from": (vacancy.get("salary") or {}).get("from"),
            "salary_to": (vacancy.get("salary") or {}).get("to"),
            "url": vacancy.get("alternate_url"),
        })
parse_vacancies()