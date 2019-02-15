from django.contrib import admin

# Register your models here.

from .models import Card

class CardAdmin(admin.ModelAdmin):
        list_display = ('__unicode__', 'answer_tag', 'station' )
        search_fields = ['question']

admin.site.register(Card, CardAdmin)
