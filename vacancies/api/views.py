from django.db.models import Avg, Count
from django.db.models.functions import TruncDate

from vacancies.models import VacancyModel

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

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
    

class VacancyTrendsView(APIView):
    """
    return
    Example: [{"date": "2025-11-01", "vacancies": 42}, ...]
    """

    def get(self, request):
        trends = (
            VacancyModel.objects
            .annotate(date_only=TruncDate('date'))  # округляем до дня
            .values('date_only')
            .annotate(vacancies=Count('id'))
            .order_by('date_only')
        )

        # Преобразуем дату в строку, иначе JSON не сможет её сериализовать
        data = [
            {
                "date": item["date_only"].strftime("%Y-%m-%d") if item["date_only"] else None,
                "vacancies": item["vacancies"],
            }
            for item in trends
        ]

        return Response(data)
            