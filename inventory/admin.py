from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Item)

class viewAdmin(admin.ModelAdmin):
    pass