from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'phone_number',
        'created_at',
    )

    search_fields = (
        'user__username',
        'phone_number',
    )

    ordering = (
        'user__username',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    fieldsets = (
        (
            'User Information',
            {
                'fields': (
                    'user',
                    'phone_number',
                    'address',
                    'profile_image',
                )
            }
        ),
        (
            'Dates',
            {
                'fields': (
                    'created_at',
                    'updated_at',
                )
            }
        ),
    )