from __future__ import unicode_literals
from django.core.management.base import BaseCommand

from core.import_secondary import import_secondary_schools


class Command(BaseCommand):

    help = "Import secondary schools from .csv file"

    def handle(self, *args, **options):
        import_secondary_schools()
