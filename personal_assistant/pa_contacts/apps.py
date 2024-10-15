from django.apps import AppConfig


class ContactsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pa_contacts'
    verbose_name = 'Contacts'
    description = '''Allows users to manage their contact list with CRUD operations, including organizing by birthdays and searching by name.
This web application is designed to manage contacts and perform full CRUD (Create, Read, Update, Delete) operations on them. Each contact entry contains several fields: name, physical address, email address, phone number, and date of birth. A key feature of the application is a dedicated section that displays upcoming birthdays based on the date of birth field. Users can view birthday notifications for contacts over three selectable timeframes: the next week, the next month, or the next three months.
Additionally, the application provides a search functionality, allowing users to quickly locate specific contacts by searching for their names. This feature ensures efficient navigation through potentially large contact lists and enhances user experience by streamlining access to contact information.'''
    icon = 'person-vcard-fill'
