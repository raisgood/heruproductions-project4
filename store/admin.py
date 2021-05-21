from django.contrib import admin
from .models import Library

# Register your models here.
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'writer', 'description');

admin.site.register(Library, LibraryAdmin)
