from modeltranslation.translator import translator, TranslationOptions
from .models import Service, Project, Client, Order, ContactMessage


class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class ClientTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')


class OrderTranslationOptions(TranslationOptions):
    fields = ('project_description',)


class ContactMessageTranslationOptions(TranslationOptions):
    fields = ('name', 'message')


translator.register(Service, ServiceTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
translator.register(Client, ClientTranslationOptions)
translator.register(Order, OrderTranslationOptions)
translator.register(ContactMessage, ContactMessageTranslationOptions)
