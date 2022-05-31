from django.contrib import admin

from .models import FirstModel

# Register your models here.

class FirstModelAdmin(admin.ModelAdmin):
    list_display=("name",)

admin.site.register(FirstModel, FirstModelAdmin)

# Register your models here.
