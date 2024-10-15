from django.apps import AppConfig


class PaFileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pa_file'
    verbose_name = 'Files'
    description = '''Allows file uploads and viewing, securely storing content in the cloud and enabling filtering and sorting via a tag-like system.
Another significant feature of the application is file management, which allows users to upload and view files. Although this functionality may seem straightforward, it is designed with reliability in mind, as all uploaded files are securely stored on a third-party cloud service. This ensures that user content is safely preserved, with the added benefit of cloud-based security and scalability.
Additionally, the file management feature has its own tagging system, similar to the one used for contacts and notes. These "tags" enable users to filter and sort their files based on assigned categories or keywords. This tagging system enhances organization by making it easier to locate specific files, even within large collections. The combination of secure cloud storage and a flexible tagging system ensures that users can manage and retrieve their files efficiently.'''
    icon = 'file-earmark-fill'
