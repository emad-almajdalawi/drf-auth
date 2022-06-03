from django.contrib import admin
from .models import Meme, MemeNoImg

@admin.register(Meme)
class AdminMeme(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at', 'updated_at')
    list_filter = ('owner',)
    search_fields = ('name', 'owner', 'id')


@admin.register(MemeNoImg)
class AdminMeme(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at', 'updated_at')
    list_filter = ('owner',)
    search_fields = ('name', 'owner', 'id')

