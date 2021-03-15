from django.contrib import admin
from .models import Library

# Register your models here.
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'writer', 'description', 'publish_date', 'price', 'stock');

admin.site.register(Library, LibraryAdmin)
