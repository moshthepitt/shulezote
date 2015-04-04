from __future__ import unicode_literals
from django.core.management.base import BaseCommand

from core.import_ksce import import_kcse_results


class Command(BaseCommand):

    help = "Import KCSE results from .csv file"

    def handle(self, *args, **options):
        import_kcse_results()
