from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('username', 'email')
    readonly_fields = ('created_at',)

