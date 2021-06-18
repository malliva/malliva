from django.contrib import admin
from .models import CustomField, CustomFieldItem

# Register your models here.

admin.site.register(CustomField)
admin.site.register(CustomFieldItem)
