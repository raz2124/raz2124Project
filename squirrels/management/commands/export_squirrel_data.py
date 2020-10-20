import csv
from django.core.management.base import BaseCommand, CommandError
from squirrels.models import Squirrel

class Command(BaseCommand):
    help = 'Export squirrel data'
    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help='file containing squirrel data')

    def handle(self, *args, **options):
        file_ = options['squirrel_file']

        
        with open(file_, 'w') as fp:
            writer = csv.writer(fp)
            writer.writerow(['X','Y','Unique Squirrel ID','Shift', 'Date','Age'])

            for squirrel in Squirrel.objects.all().values_list('latitude','longitude','unique_id','shift','date','age'):
                writer.writerow(squirrel)
        
        
        msg = f'You are exporting to {file_}'
        self.stdout.write(self.style.SUCCESS(msg))
