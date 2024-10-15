from django.apps import AppConfig


class PaUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pa_user'
    verbose_name = 'Users'
    description = '''Manages user authentication, including registration, login, and password recovery, ensuring personalized access to data and features while protecting against spam accounts.
The user management feature serves as the foundation for all other functionalities within the application. Each of the previously mentioned entities—contacts, notes, files, news, and even tags—are linked to specific users. This ensures that, upon logging into the application, users can only view and interact with their own data, providing a personalized and secure experience.
In addition to data segregation, the application includes the essential user authentication processes: registration, login, and password recovery. User registration is moderated, adding a layer of protection against spam accounts and ensuring that only legitimate users gain access to the system. This moderation helps maintain the integrity and security of the application.
For non-registered users, access to the application is highly restricted, with most features unavailable. However, once a user completes registration and gains approval, they are granted access to the full suite of functionalities, unlocking the application's broad capabilities and enhancing their ability to manage contacts, notes, files, and more efficiently. This user-centered approach ensures a secure and tailored experience for every individual.'''
    icon = 'people-fill'
    not_in_main_menu = True

    def ready(self) -> None:
        from . import signals  # noqa
