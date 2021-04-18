from django.db import models

# Create your models here.
class Todo(models.Model):
    id = models.IntegerField(primary_key=True)
    Country = models.CharField(max_length=100, db_column='Country,Other', default='country')
    TotalCases = models.CharField(max_length=100, db_column='TotalCases', default='cases')
    New_cases = models.CharField(max_length=100, db_column='NewCases', default='new cases')
    total_Deaths = models.CharField(max_length=100, db_column='TotalDeaths', default='total deaths')
    new_deaths = models.CharField(max_length=100, db_column='NewDeaths', default='new deaths')
    total_recovered = models.CharField(max_length=100, db_column='TotalRecovered', default='total recovered')
    new_recovered = models.CharField(max_length=100, db_column='NewRecovered', default='new recovered')
    active_cases = models.CharField(max_length=100, db_column='ActiveCases', default='active cases')
    serious = models.CharField(max_length=100, db_column='Serious,Critical', default='serious cases')
    total_cases_percent = models.CharField(max_length=100, db_column='Tot Cases/1M pop', default='total case/1M pop')
    deaths_percent = models.CharField(max_length=100, db_column='Deaths/1M pop', default='deaths/1M pop')
    total_tests = models.CharField(max_length=100, db_column='TotalTests', default='total tests')
    tests_percent = models.CharField(max_length=100, db_column='Tests/ 1M pop', default='tests/1M pop')
    population = models.CharField(max_length=100, db_column='Population', default='population')
    continent= models.CharField(max_length=100, db_column='Continent', default='continent')
    CaseEveryXppl=models.CharField(max_length=100, db_column='1 Caseevery X ppl', default='CaseEveryXppl')
    DeathEveryXppl=models.CharField(max_length=100, db_column='1 Deathevery X ppl', default='DeathEveryXppl')
    TesteveryXppl= models.CharField(max_length=100, db_column='1 Testevery X ppl', default='TesteveryXppl')
    objects: models.Manager()
    class Meta:
       db_table="web_crawler"

class Covid(models.Model):
    updated = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=100)
    countryInfo = models.CharField(max_length=100)
    cases = models.CharField(max_length=100)
    todayCases = models.CharField(max_length=100)
    deaths = models.CharField(max_length=100)
    todayDeaths = models.CharField(max_length=100)
    recovered = models.CharField(max_length=100)
    todayRecovered = models.CharField(max_length=100)
    active = models.CharField(max_length=100)
    critical = models.CharField(max_length=100)
    casesPerOneMillion = models.CharField(max_length=100)
    deathsPerOneMillion = models.CharField(max_length=100)
    tests = models.CharField(max_length=100)
    testsPerOneMillion = models.CharField(max_length=100)
    population= models.CharField(max_length=100)
    continent=models.CharField(max_length=100)
    oneCasePerPeople=models.CharField(max_length=100)
    oneDeathPerPeople= models.CharField(max_length=100)
    activePerOneMillion=models.CharField(max_length=100)
    recoveredPerOneMillion= models.CharField(max_length=100)
    criticalPerOneMillion= models.CharField(max_length=100)
    objects: models.Manager()
    class Meta:
       db_table="api_covid_data"




"""
    def __str__(self):
        return self"""