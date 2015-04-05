from __future__ import unicode_literals
from django.core.management.base import BaseCommand

from core.import_kcse_failed import process_passed


class Command(BaseCommand):

    help = "Import KCSE results from previously failed .csv file"

    def handle(self, *args, **options):
        process_passed()
