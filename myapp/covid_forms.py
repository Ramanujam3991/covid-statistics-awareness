from django import forms
from .models import Covid
CHART_CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart'),
)

RESULT_CHOICES = (
    ('#1', 'API DATA'),
    ('#2', 'WEB CRAWLER DATA'),
    ('#3', 'SCIPY'),
    ('#4', 'ML PREDICTION'),
)

RESULT_CHOICES_COLUMN = (
    ('#1', 'Total Cases'),
    ('#2', 'Total Deaths'),
    ('#3', 'Total Recovered'),
    ('#4', 'New Cases'),
    ('#5', 'New Deaths'),
    ('#6', 'New Recovered Tomorrow'),
)

class CovidSearchForm(forms.Form):
    #date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    #date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    column_list = forms.ChoiceField(choices=RESULT_CHOICES_COLUMN)
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
    data_source = forms.ChoiceField(choices=RESULT_CHOICES)
    class Meta:
        model = Covid
        widgets = {'column_list': forms.Select(attrs={'class': 'data'})}
