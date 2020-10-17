import csv
from django.core.management.base import BaseCommand, CommandError
from squirrels.models import Squirrel

class Command(BaseCommand):
    help = 'Import squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help='file containing squirrel data')

    def handle(self, *args, **options):
        file_ = options['squirrel_file']
       
        with open(file_) as fp:
            reader = csv.DictReader(fp)

            for item in reader:
                obj = Squirrel()
                obj.unique_id=item['Unique Squirrel ID']
                obj.shift = item['Shift']
                obj.age = item['Age']
                obj.latitutde = item['X']
                obj.longitude = item['Y']
                obj.date = item['Date']
                obj.save()
       
        msg = f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))


