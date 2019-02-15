from django.contrib import admin
from .models import Module310Card

#admin.site.register(Module308Card)
# Register your models here.

class CardAdmin(admin.ModelAdmin):
        list_display = ('__unicode__', 'answer' )
        search_fields = ['question']

admin.site.register(Module310Card, CardAdmin)
