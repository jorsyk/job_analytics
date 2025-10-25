from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from vacancies.models import VacancyModel
from vacancies.serializers import VacancySerializer
from vacancies.filters import VacancyFilter


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = VacancyModel.objects.all().order_by("-date", "-id")
    serializer_class = VacancySerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = VacancyFilter