from django.apps import AppConfig


class PaNoteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pa_note'
    verbose_name = 'Notes'
    description = '''The application also includes a notes feature, where each note consists of a title and a description. While simple in structure, notes are tightly integrated with the tagging functionality. This allows users to assign tags to notes, offering more precise categorization and organization. By linking notes to tags, users can characterize and group their notes based on shared topics, themes, or categories.
In addition to basic title-based searching, notes offer a powerful combined search function. Users can search for notes not only by their titles but also by the tags associated with them. This dual search capability enhances the discoverability of notes, enabling users to quickly find relevant information by filtering notes through both their titles and tags. The result is a more dynamic and flexible note management system that improves efficiency and organization.'''
