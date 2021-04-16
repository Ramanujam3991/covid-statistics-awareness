from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.IntegerField(primary_key=True)
    Country = models.CharField(max_length=100, default='country')
    TotalCases = models.CharField(max_length=100, default='cases')
    New_cases = models.CharField(max_length=100, default='new cases')
    total_Deaths = models.CharField(max_length=100, default='total deaths')
    new_deaths = models.CharField(max_length=100, default='new deaths')
    total_recovered = models.CharField(max_length=100, default='total recovered')
    active_cases = models.CharField(max_length=100, default='active cases')
    serious = models.CharField(max_length=100, default='serious cases')
    total_cases_percent = models.CharField(max_length=100, default='total case/1M pop')
    deaths_percent = models.CharField(max_length=100, default='deaths/1M pop')
    total_tests = models.CharField(max_length=100, default='total tests')
    tests_percent = models.CharField(max_length=100, default='tests/1M pop')
    population = models.CharField(max_length=100, default='population')
    continent= models.CharField(max_length=100, default='continent')
    CaseEveryXppl=models.CharField(max_length=100, default='population')
    DeathEveryXppl=models.CharField(max_length=100, default='population')
    TesteveryXppl= models.CharField(max_length=100, default='population')
    objects: models.Manager()

    class Meta:
        db_table="web_crawler"




"""
    def __str__(self):
        return self"""