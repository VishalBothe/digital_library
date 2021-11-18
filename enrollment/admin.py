from django.contrib import admin
from .models import Enrollment 

# Register your models here.
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('enrollment_id','user','book')
    list_filter = ('book',)
    search_fields = ('user', 'book')