import requests
from django.core.management.base import BaseCommand
from vacancies.models import VacancyModel


class Command(BaseCommand):
    help = " Parsing vacancies and save to database"

    def add_arguments(self, parser):
        pass