from django.contrib import admin
from .models import *

# Register your models here.




class CarAdmin(admin.ModelAdmin):
    # Display these columns in the table list view
    list_display = ('make','model','color','price','is_available')

    # Add search capability on the name and description fields
    search_fields = ('make', 'color')

    # Enable filters based on certain fields
    list_filter = ('price','color')

# Register the model and custom admin class
admin.site.register(Car, CarAdmin)



