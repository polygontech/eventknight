from django.contrib import admin
from .models import Event, User


# Register your models here.
class UserInline(admin.TabularInline):
    model = User
    fieldsets = [
        ('Twitter Username', {'fields': ['tw_user']}),
        ('Twitter Access Token', {'fields': ['tw_user_token']}),
        ('Twitter Access Token Secret', {'fields': ['tw_user_token_secret']}),
    ]


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Event Name', {'fields': ['event_name']}),
        ('Event Tags', {'fields': ['event_tags']}),
    ]

    inlines = [UserInline]


admin.site.register(Event, EventAdmin)
