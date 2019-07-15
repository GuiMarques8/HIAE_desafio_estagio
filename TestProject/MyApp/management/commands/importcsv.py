from MyApp.models import Fenotipos
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        insert_count = Fenotipos.datas.from_csv(
            'MyApp/utils/fenotipos_genes.csv', delimiter=';')
        print("{} records inserteds".format(insert_count))
