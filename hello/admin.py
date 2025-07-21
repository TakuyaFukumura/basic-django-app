from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Message モデルの管理画面設定
    """
    list_display = ('content', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('content',)
    list_editable = ('is_active',)
    ordering = ('-created_at',)
    
    fieldsets = (
        ('メッセージ情報', {
            'fields': ('content', 'is_active')
        }),
        ('日時情報', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')
