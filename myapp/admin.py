from django.contrib import admin

# Register your models here.
from .models import Candidates,Countries, Jobs, Agents  # Make sure this matches your actual model name



@admin.register(Candidates)
class Candidates(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'job_applied', 'date_of_birth')
    search_fields = ('full_name','email', 'nin_number', 'passport_number')
    list_filter = ('gender', 'marital_status', 'job_location')

@admin.register(Countries)
class Countries(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)  
    list_filter = ('name',)  

@admin.register(Jobs)
class Jobs(admin.ModelAdmin):
    list_display = ('title', 'location', 'salary', 'status', 'closing_date')
    search_fields = ('title', 'company', 'location')
    list_filter = ('status', 'location')

@admin.register(Agents)
class Agents(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'gender')
    search_fields = ('full_name', 'email', 'phone_number')
    list_filter = ('gender',)
