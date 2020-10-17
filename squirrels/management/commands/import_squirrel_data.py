import csv
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Import squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help='file containing squirrel data')

    def handle(self, *args, **options):
        file_ = options['squirrel_file']
       
        with open(file_) as fp:
            reader = csv.DictReader(fp)

            for item in reader:
                pass
       
       msg = f'You are importing from {file}'
        self.stdout.write(self.style.SUCCESS(msg))


