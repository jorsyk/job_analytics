from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend

from vacancies.models import VacancyModel
from vacancies.api.serializers import VacancySerializer, AvgSalarySerializer
from vacancies.api.filters import VacancyFilter


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = VacancyModel.objects.all().order_by("-date", "-id")
    serializer_class = VacancySerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = VacancyFilter


class AvgSalaryView(APIView):
    """
        return avg salary
    """
    def get(self, request):
        avg_salary = VacancyModel.objects.aaggregate(Avg('salary_from'))['salary_from_avg']

    # if db is empty
        avg = float(avg_salary) if avg_salary is not None else 0.0

        return Response({"avg_salary": avg_salary})