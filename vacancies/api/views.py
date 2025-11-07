from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg, Count
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
        
        result = VacancyModel.objects.aggregate(avg_salary=Avg('salary_from'))

        avg = float(result['avg_salary']) if result['avg_salary'] is not None else 0.0

        return Response({"avg_salary": avg})
    

class TopCitiesView(APIView):
    """
    retutn top 5 cities
    """
    def get(self, request):
        data = (
            VacancyModel.objects
            .values("city")                     
            .annotate(count=Count("city"))      
            .order_by("-count")[:5]             
        )
        return Response(data)