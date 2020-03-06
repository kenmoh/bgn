from django.contrib import admin
from .models import Post, Event, About, Objective, Executive, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'place_of_work', 'subject', 'message')

class ExecutiveAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'about_me')


admin.site.register(Post)
admin.site.register(Event)
admin.site.register(About)
admin.site.register(Objective)
admin.site.register(Executive, ExecutiveAdmin)
admin.site.register(Contact, ContactAdmin)
