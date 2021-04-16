from django import forms
from .models import Todo
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['id', 'Country', 'TotalCases','New_cases','total_Deaths','new_deaths','total_recovered','active_cases','serious','total_cases_percent','deaths_percent','total_tests','tests_percent','population','continent','CaseEveryXppl','DeathEveryXppl','TesteveryXppl'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'id': forms.TextInput(attrs={ 'class': 'form-control' }),
            'Country,Other': forms.TextInput(attrs={ 'class': 'form-control' }),
            'TotalCases': forms.TextInput(attrs={ 'class': 'form-control' }),
            'NewCases': forms.TextInput(attrs={ 'class': 'form-control' }),
            'TotalDeaths': forms.TextInput(attrs={ 'class': 'form-control' }),
            'NewDeaths': forms.TextInput(attrs={ 'class': 'form-control' }),
            'TotalRecovered': forms.TextInput(attrs={ 'class': 'form-control' }),
            'ActiveCases': forms.TextInput(attrs={ 'class': 'form-control' }),
            'Serious,Critical': forms.TextInput(attrs={ 'class': 'form-control' }),
            'Tot Cases/1M pop': forms.TextInput(attrs={ 'class': 'form-control' }),
            'Deaths/1M pop': forms.TextInput(attrs={ 'class': 'form-control' }),
            'TotalTests': forms.TextInput(attrs={ 'class': 'form-control' }),
            'Tests/ 1M pop': forms.TextInput(attrs={ 'class': 'form-control' }),
            'Population': forms.TextInput(attrs={ 'class': 'form-control' }),
            'Continent': forms.TextInput(attrs={ 'class': 'form-control' }),
            '1 Caseevery X ppl': forms.TextInput(attrs={ 'class': 'form-control' }),
            '1 Deathevery X ppl': forms.TextInput(attrs={ 'class': 'form-control' }),
            '1 Testevery X ppl': forms.TextInput(attrs={ 'class': 'form-control' }),
      }