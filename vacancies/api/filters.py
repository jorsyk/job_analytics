import django_filters
from vacancies.models import VacancyModel

class VacancyFilter(django_filters.FilterSet):
    class Meta:
        model = VacancyModel
        fields = ['city', 'company']