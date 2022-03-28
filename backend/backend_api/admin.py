from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list = ('title', 'author', 'isbn')

    admin.site.register(Book)