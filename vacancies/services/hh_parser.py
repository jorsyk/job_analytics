import requests
from dateutil import parser

def fetch_vacancies(text: str = "python", pages: int = 2) -> list[dict]:
    
    base_url = "https://api.hh.ru/vacancies"
    all_vacancies = []
    try:
        for page in range(pages):
            params = {"text": text, "page": page, "per_page": 100}
            response = requests.get(base_url, params=params, timeout=10)
    
            if response.status_code != 200:
                print(f"Ошибка: {response.status_code} — {response.text}")
                break

            data = response.json()
            vacancies = data.get("items", [])
    
            for vacancy in vacancies:
                salary = vacancy.get("salary") or {}
                roles = vacancy.get("professional_roles") or []
                published = vacancy.get("published_at")

                all_vacancies.append({
                    "title": vacancy.get("name"),
                    "company": vacancy.get("employer", {}).get("name"),
                    "city": vacancy.get("area", {}).get("name"),
                    "salary_from": salary.get("from"),
                    "salary_to": salary.get("to"),
                    "currency": salary.get("currency"),
                    "role": roles[0].get("name") if roles else None,
                    "url": vacancy.get("alternate_url"),
                    "published_at": parser.parse(published) if published else None
                })

            if len(vacancies) < 100:
                break

    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    
    return all_vacancies

if __name__ == "__main__":
    vacancies = fetch_vacancies("django developer", pages=3)
    print(f"Всего получено: {len(vacancies)} вакансий")

    # Пример одной записи
    print(vacancies[0])
