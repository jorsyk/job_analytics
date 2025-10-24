from rest_framework import viewsets
from vacancies.models import VacancyModel
from vacancies.serializers import VacancySerializer

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = VacancyModel.objects.all().order_by("-date", "-id")
    serializer_class = VacancySerializer
