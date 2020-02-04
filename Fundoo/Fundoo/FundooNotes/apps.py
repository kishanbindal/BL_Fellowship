from django.apps import AppConfig


class FundoonotesConfig(AppConfig):
    name = 'FundooNotes'

    def ready(self):
        from . import schedule
        schedule.start()