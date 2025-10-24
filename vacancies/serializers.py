from rest_framework import serializers
from vacancies.models import VacancyModel

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyModel
        fields = ["id", "title", "company", "salary_from", "salary_to", "date", "url"]
