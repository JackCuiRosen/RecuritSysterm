import csv

from django.core.management import BaseCommand

from jobs.models import Job



class Command(BaseCommand):
    help = '导入Job数据'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path, 'rt', encoding='gbk') as f:
            reader = csv.reader(f)
            # k = 0

            for row in reader:
                job = Job.objects.create(
                    JobName = row[0][1:len(row[0]) - 1],
                    WorkPlace = row[1],
                    WorkKind = row[2],
                    JobID = row[3],
                    JobDescrib = row[4],
                    JobRequire = row[5]

                )
                print(job)

