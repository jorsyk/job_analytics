from rest_framework import serializers
from vacancies.models import VacancyModel

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = VacancyModel
        fields = ["id", "title", "company", "city", "salary_from", "url", "date"]


class AvgSalarySerializer(serializers.Serializer):
    avg_salary = serializers.DecimalField(max_digits=10, decimal_places=2, allow_null=True)