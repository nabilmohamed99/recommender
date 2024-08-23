from django.contrib import admin

# Register your models here.
from .models import Movies

class MoviesAdmin(admin.ModelAdmin):
    list_display = ['__str__','calculate_ratings_count']
    readonly_fields = ['calculate_ratings_count']
admin.site.register(Movies,MoviesAdmin)
