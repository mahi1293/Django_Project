from __future__ import unicode_literals

from django.apps import AppConfig
from material.frontend.apps import ModuleMixin


class PliteSpotsConfig(ModuleMixin, AppConfig):
    name = 'plite_spots'
    icon = '<i class="mdi-communication-quick-contacts-dialer"></i>'
