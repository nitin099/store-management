import csv
from django.core.management import BaseCommand
from customers.models import Customer


class Command(BaseCommand):
    help = 'Load a customers csv file into the database'

    def add_arguments(self, parser):
        """
        Adds the argument from command line.
        """
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        """
        Inserts the csv data to the Customer model.
        """
        path = kwargs['path']
        with open(path, 'r',) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            try:
                for row in csv_reader:
                    Customer.objects.update_or_create(
                        email=row[3],
                        defaults={
                            'first_name': row[0],
                            'last_name': row[1],
                            'phone': row[4],
                            'currency': row[5],
                            'created_at': row[6],
                            'updated_at': row[7]
                        }
                    )
            except Exception as e:
                print(str(e))
