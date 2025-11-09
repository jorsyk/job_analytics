from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from vacancies.api import views

router = routers.DefaultRouter()
router.register(r"api/vacancies", views.VacancyViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("api/stats/salary/", views.AvgSalaryView.as_view(), name="avg-salary"),
    path("api/stats/top-cities/", views.TopCitiesView.as_view(), name="top-cities"),
    path("api/stats/trends/", views.VacancyTrendsView.as_view(), name="vacancy-trends"),
]
