from django.contrib import admin
from .models import PlayStore
# Register your models here.


@admin.register(PlayStore)
class PlayStoreAdmin(admin.ModelAdmin):
    class Media:
        js = ('descriptionBox.js', )
