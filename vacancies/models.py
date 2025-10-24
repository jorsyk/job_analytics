from django.db import models

class VacancyModel(models.Model):
    title = models.CharField(max_length=255, null=False)
    company = models.CharField(max_length=255, null=False)
    salary_from = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    url = models.URLField(null=False)
    date = models.DateField()
