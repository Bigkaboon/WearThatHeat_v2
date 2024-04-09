from django.contrib import admin
from contact.models import Contact, NewsLetter


class ContactAdmin(admin.ModelAdmin):
    """Allows admin to manage enquiries via the admin panel"""
    list_display = (
        'name',
        'email',
        'enquiry_type',
        'date',
    )

class NewsLetterAdmin(admin.ModelAdmin):
    """Allows admin to view who signed up for news letter"""
    list_display = (
        'email',
    )


admin.site.register(Contact, ContactAdmin)
admin.site.register(NewsLetter, NewsLetterAdmin)
