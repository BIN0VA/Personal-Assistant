from django.apps import AppConfig


class PaNewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pa_news'
    verbose_name = 'News'
    description = '''Displays global news and currency exchange rates, with real-time data and a caching system for faster load times, including a superuser-controlled data sync.
The application also includes a distinct feature for displaying news and currency exchange rates, providing a broader range of information compared to other functionalities. The news section delivers information about global events sourced from external news websites. In addition to traditional news, the application displays real-time currency exchange rates, specifically highlighting them in a dedicated area of the navigation panel. These rates are visible on all pages for quick reference. There is also a separate page showing detailed dollar exchange rates across various banks, providing users with a comparative view.
Traditional news articles are displayed primarily on the home page, in a section at the bottom, making it easy for users to stay updated without leaving the main interface. Furthermore, the application has a special page where superusers can fetch data from external news sources and currency rate providers, syncing it with the application's database. By storing this information locally, the system accelerates page loading times for users, effectively implementing a form of caching. This feature allows the application to present fresh content while ensuring performance and reliability across the platform.'''
    icon = 'newspaper'
