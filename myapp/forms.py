from django import forms
from .models import Todo
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['id', 'Country', 'TotalCases','New_cases','total_Deaths','new_deaths','total_recovered','new_recovered','active_cases','serious','total_cases_percent','deaths_percent','total_tests','tests_percent','population','continent','CaseEveryXppl','DeathEveryXppl','TesteveryXppl'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
