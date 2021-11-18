from django.contrib import admin
from .models import CustomUser 

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','is_subscriber','due_date')
    list_filter = ('is_subscriber',)
    empty_value_display = '-empty-'

    fieldset = (
        ('Required Information', {
            'description':"These fields are required for each user",
            'fields':('name','email','mobile','password'),
        }),
        ('Optional Information', {
            'classes':('collapse',),
            'fields':('is_subscriber','due_date'),
        })
    )