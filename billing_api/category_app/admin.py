from django.contrib import admin

from category_app.models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):  
    list_display = ('designation', 'description', 'date_created', 'date_updated') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Category, CategoryAdmin) 