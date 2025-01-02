from django.core.management.base import BaseCommand,CommandError

class Command(BaseCommand):
    help = 'Description of the command'

    def handle(self, *args, **options:any)-> str| None:
        self.stdout.write('Command called')

    