from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'user'

    def ready(self):
        import user.signals