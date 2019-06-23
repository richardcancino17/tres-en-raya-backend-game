from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from social_django.models import *
from rest_framework.authtoken.admin import Token


class PlayerAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': (
            'email', 'password', 'is_superuser')}),
        (('Important dates'),
         {'fields': ('last_login', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ['username', 'id', 'email', 'is_active', 'created_at']
    list_filter = ('is_active',)
    search_fields = ('email',)
    ordering = ('email', 'id')
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(Player, PlayerAdmin)
admin.site.unregister(Association)
admin.site.unregister(Nonce)
admin.site.unregister(UserSocialAuth)
admin.site.unregister(Group)
admin.site.unregister(Token)
