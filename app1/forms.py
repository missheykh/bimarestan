from django import forms
from django.forms import ModelForm
from .models import Company,Hospital,people


class signin_form(forms.Form):
    name=forms.CharField(max_length=30)
    national_code=forms.CharField(max_length=10)
    hospital=forms.ModelChoiceField(queryset=Hospital.objects.all())
    company=forms.ModelChoiceField(queryset=Company.objects.all())
    covid_test=forms.BooleanField()
    phone_number = forms.CharField(max_length=11)
    #  class Meta:
    #     model = people
    #     fields = ['name', 'nationalcode', 'hospital', 'company','covidtest','phone']

class search_hospital_people(forms.Form):
    HospitalName=forms.ModelChoiceField(queryset=Hospital.objects.all())



class search_company_people(forms.Form):
    CompanyName=forms.ModelChoiceField(queryset=Company.objects.all())