from django.db import models

class VacancyModel(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True, blank=True)
    salary_from = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_to = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    url = models.URLField(unique=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.title} — {self.company}"