
from django.contrib import admin
from django.urls import path,include
from .views import signin,show_hospital_people,show_company_people

app_name="app1"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("signin/",signin.as_view(),name="signin"),
    path("show_hospital_people/",show_hospital_people,name="show_hospital_people"),
    path("show_company_people/",show_company_people,name="show_company_people"),

]


