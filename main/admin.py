from django.contrib import admin
from .models import Table

class TableAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'quantity', 'distance')
    # fields = (('rubric', 'author'), 'title', 'content', 'price', #'rubric' и 'author' вывели в одну строку для удобства.
    #           'contacts', 'image', 'is_active')


admin.site.register(Table, TableAdmin)
