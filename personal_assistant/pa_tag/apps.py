from django.apps import AppConfig


class PaTagConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pa_tag'
    verbose_name = 'Tags'
    description = '''Enables users to create and delete tags, with restrictions on deletion if the tag is in use, and shared across all users.
The application includes a tagging feature that allows users to assign tags to contacts, providing a way to categorize and organize them more efficiently. Tags can be created and deleted, but the deletion functionality is unique. Specifically, users cannot delete a tag if it is currently being used by any contact, ensuring that no data becomes disorganized or improperly categorized. This rule enforces data consistency and prevents accidental removal of important tags.
Moreover, tags created by one user are not restricted to just that user; they are shared across the entire system. This means that any tag created by one user can be utilized by all other users, fostering collaboration and consistency in how contacts are categorized throughout the application. This shared tagging system enhances the flexibility and usability of the application.'''
    icon = 'tags-fill'
