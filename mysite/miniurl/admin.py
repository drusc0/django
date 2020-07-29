from django.contrib import admin
from .models import Miniurl


@admin.register(Miniurl)
class MiniurlAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_url', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ('original_url',)
