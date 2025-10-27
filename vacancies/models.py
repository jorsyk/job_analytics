from django.db import models

class VacancyModel(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    salary_from = models.IntegerField(null=True, blank=True)
    salary_to = models.IntegerField(null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.company})"