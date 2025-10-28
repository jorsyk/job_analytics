import requests
from django.core.management.base import BaseCommand
from vacancies.models import VacancyModel


class Command(BaseCommand):
    help = " Parsing vacancies and save data to database"

    def add_arguments(self, parser):
        parser.add_argument(
            "query",
            type=str,
            help="Vacancy title for seach",
        )
    
    def handle(self, *args, **options):
        query = options["query"]
        self.stdout.write(self.style.NOTICE(f"Parsing vacancy for request: {query}"))

        url = "https://api.hh.ru/vacancies"
        params = {"text": query, "per_page": 100}

        response = requests.get(url, params=params)
        data = response.json()

        count = 0
        for item in data.get("items", []):
            title = item.get("name")
            company = item.get("employer", {}).get("name")
            city = item.get("area", {}).get("name")
            salary = item.get("salary", {})
            salary_from = salary.get("from") if salary else None
            vacancy_url = item.get("alternate_url")

            # Save to db
            VacancyModel.objects.update_or_create(
                title=title,
                company=company,
                defaults={
                    "city": city,
                    "salary_from": salary_from,
                    "url": vacancy_url,
                },
            )
        count=+1
        
        self.stdout.write(self.style.SUCCESS(f"Загружено {count} вакансий"))