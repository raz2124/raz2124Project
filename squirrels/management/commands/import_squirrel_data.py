import csv
from django.core.management.base import BaseCommand, CommandError
from squirrels.models import Squirrel
import datetime

class Command(BaseCommand):
    help = 'Import squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help='file containing squirrel data')

    def handle(self, *args, **options):
        file_ = options['squirrel_file']
       
        with open(file_) as fp:
            reader = csv.DictReader(fp)
            for item in reader:
                if item['Unique Squirrel ID'] in list(Squirrel.objects.order_by().values_list('unique_id',flat=True).distinct()):
                    pass
                else:
                    obj = Squirrel()
                    obj.latitude = item['Y']
                    obj.longitude = item['X']
                    obj.unique_id=item['Unique Squirrel ID']
                    obj.shift = item['Shift']
                    obj.date = datetime.datetime.strptime(item['Date'], '%m%d%Y')
                    obj.age = item['Age']
                    obj.save()

       
        msg = f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))


