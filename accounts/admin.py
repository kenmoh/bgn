from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User, BackgroundAdmin, Application, Success, Sponsor


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['id', 'username', 'first_name', 'last_name',
                    'phone', 'email', 'location', 'confirm_application', 'is_approved']
    fieldsets = (
        ('User', {'fields': ('username', 'phone',
                             'email', 'first_name', 'last_name', 'location', 'skills', 'about_me',
                             'profile_image', 'confirm_application', 'is_approved')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')})
    )

    list_filter = ['confirm_application', 'is_approved']


class SuccessAdmin(UserAdmin):
    model = User
    list_display = ['title', 'message', 'date_sent']


admin.site.register(User, UserAdmin)
admin.site.register(BackgroundAdmin)
admin.site.register(Application)
admin.site.register(Success, SuccessAdmin)
admin.site.register(Sponsor)

