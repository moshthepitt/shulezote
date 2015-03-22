from __future__ import unicode_literals
from django.core.management.base import BaseCommand

from core.import_primary import import_primary_schools

class Command(BaseCommand):

    help = "Import primary schools from .csv file"

    def handle(self, *args, **options):
        import_primary_schools()
