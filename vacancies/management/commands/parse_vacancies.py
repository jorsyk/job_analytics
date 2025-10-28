import time
import requests
from django.core.management.base import BaseCommand
from vacancies.models import VacancyModel

class Command(BaseCommand):
    help = "Parse vacansy with hh.ru and save data to db"


    def add_arguments(self, parser):
        parser.add_argument(
            "query",
            type=str,
            help="title for searching",
        )

    def handle(self, *args, **options):
        query = options["query"]
        self.stdout.write(self.style.WARNING(f"🔎 Parsing for request: {query}"))

        url = "https://api.hh.ru/vacancies"
        params = {"text": query, "per_page": 100}
        count = 0

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status() 
            data = response.json()

            for item in data.get("items", []):
                title = item.get("name")
                company = item.get("employer", {}).get("name")
                city = item.get("area", {}).get("name")
                salary = item.get("salary", {})
                salary_from = salary.get("from") if salary else None
                vacancy_url = item.get("alternate_url")

                VacancyModel.objects.update_or_create(
                    title=title,
                    company=company,
                    defaults={
                        "city": city,
                        "salary_from": salary_from,
                        "url": vacancy_url,
                    },
                )
                count += 1

        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f"❌ Network error: {e}"))
            time.sleep(5)
            return

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"⚠️ Unexpected error: {e}"))
            return

        self.stdout.write(self.style.SUCCESS(f"✅ Uploaded {count} vacancies"))

