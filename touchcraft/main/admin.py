from django.contrib import admin
from .models import Service, Project, Client, Order, ContactMessage


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order')
    ordering = ('display_order',)
    search_fields = ('title',)
    list_editable = ('display_order',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'link')
    ordering = ('-created_at',)
    search_fields = ('title', 'description')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'created_at')
    ordering = ('-created_at',)
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'service', 'created_at')
    ordering = ('-created_at',)
    search_fields = ('project_description', 'client__first_name', 'client__last_name')
    list_filter = ('service', 'created_at')
    raw_id_fields = ('client', 'service')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    ordering = ('-created_at',)
    search_fields = ('name', 'email', 'message')
