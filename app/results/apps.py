from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ResultsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'results'
    verbose_name = _('Javoblar')
    icon = 'fa fa-star'  # Add your icon class here