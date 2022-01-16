from django.contrib import admin
from .models import people,Hospital,Company

# Register your models here.
admin.site.register(people)
admin.site.register(Hospital)
admin.site.register(Company)