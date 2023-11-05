from django.contrib import admin
from .models import Service,Contact

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'descriptions', 'created_at', 'updated_at')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone','email','message', 'created_at', 'updated_at')

# Register your models here.
admin.site.register(Service, ServiceAdmin)
admin.site.register(Contact, ContactAdmin)
