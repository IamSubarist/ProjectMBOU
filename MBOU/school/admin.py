from django.contrib import admin
from .models import *

class GlavnayaAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'created_at'
    list_display_links = 'id', 'title'
    search_fields = 'title', 'content'

class NovostiAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'created_at'
    list_display_links = 'id', 'title'
    search_fields = 'title', 'content'

class OshkoleAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'created_at'
    list_display_links = 'id', 'title'
    search_fields = 'title', 'content'

class RoditelyamAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'created_at'
    list_display_links = 'id', 'title'
    search_fields = 'title', 'content'

class UchebnayadeyatelnostAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'created_at'
    list_display_links = 'id', 'title'
    search_fields = 'title', 'content'

class KontaktyAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'created_at'
    list_display_links = 'id', 'title'
    search_fields = 'title', 'content'

admin.site.register(Glavnaya, GlavnayaAdmin)
admin.site.register(Novosti, NovostiAdmin)
admin.site.register(Oshkole, OshkoleAdmin)
admin.site.register(Roditelyam, RoditelyamAdmin)
admin.site.register(Uchebnayadeyatelnost, UchebnayadeyatelnostAdmin)
admin.site.register(Kontakty, KontaktyAdmin)