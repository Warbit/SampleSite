from django.contrib import admin
from .models import Bb, Rubric


# Register your models here.
#управляет отображением инфо в админцком сайте
class BbAdmin(admin.ModelAdmin):
    list_display = ('title','content', 'price', 'published', 'rubric') #порядок вывода последовательности полей
    list_display_links = ('title','content')
    search_fields = ('title','content')

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
