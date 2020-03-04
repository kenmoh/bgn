from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User, Application, BackgroundAdmin


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['id', 'username', 'first_name', 'last_name',
                    'phone', 'email', 'location']
    fieldsets = (
        ('User', {'fields': ('username', 'phone',
                             'email', 'first_name', 'last_name', 'location', 'skills', 'about_me', 'profile_image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')})
    )

    list_filter = []


admin.site.register(User, UserAdmin)
admin.site.register(Application)
admin.site.register(BackgroundAdmin)
