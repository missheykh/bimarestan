from http.client import HTTPResponse
from socket import CAN_BCM_TX_ANNOUNCE
from django.views.generic import ListView,DetailView
from django.shortcuts import render,HttpResponse
from .forms import signin_form,search_hospital_people,search_company_people
from django.views import View
from .models import Company, Hospital, people
from django.shortcuts import get_object_or_404

class signin(View):
    def get(self,request):
        form=signin_form()
        return render(request,"app1/people_signin.html",{"form":form})

    def post(self,request):
        form=signin_form(request.POST)
        if form.is_valid():
            name=form.cleaned_data.get("name")
            national_code=form.cleaned_data.get("national_code")
            hospital=form.cleaned_data.get("hospital")
            company=form.cleaned_data.get("company")
            covid_test=form.cleaned_data.get("covid_test")
            phone_number=form.cleaned_data.get("phone_number")

            hospital_obj=get_object_or_404(Hospital,title=hospital)   
            company_obj=get_object_or_404(Company,title=company)   

            user=people.objects.create(name=name,national_code=national_code,covid_test=covid_test,phone_number=phone_number,hospital=hospital_obj,
company=company_obj)
            return HttpResponse("user created")
        return render(request,"app1/people_signin.html",{"form":form})



def show_hospital_people(request):
        if request.method=="GET":
            form=search_hospital_people()
            ctx={"form":form}
            return render(request,"app1/hospital_people_list.html",ctx)

        if request.method=="POST":
            form=search_hospital_people(request.POST)
            if form.is_valid():
                HospitalName=form.cleaned_data.get("HospitalName")
                peaple_in_hospital=Hospital.objects.get(title=HospitalName).users.all() 
                ctx={"form":form,"peaple_in_hospital":peaple_in_hospital}                  
                return render(request,"app1/hospital_people_list.html",ctx)
    

def show_company_people(request):
    if request.method=="GET":
            form=search_company_people()
            ctx={"form":form}
            return render(request,"app1/company_people_list.html",ctx)

    if request.method=="POST":
            form=search_company_people(request.POST)
            if form.is_valid():
                CompanyName=form.cleaned_data.get("CompanyName")
                peaple_in_company=Company.objects.get(title=CompanyName).workers.all() 
                ctx={"form":form,"peaple_in_company":peaple_in_company}                  
                return render(request,"app1/company_people_list.html",ctx)

