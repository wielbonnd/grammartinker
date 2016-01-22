from django.core.management.base import BaseCommand
import csv
from apps.verbs import models as verbs_models
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def create_verb(self, verbs_row):
        infinitive = verbs_row[0]
        simple_past = verbs_row[1]
        past_participle = verbs_row[2]
        try:
            verb = verbs_models.Verb.objects.get(infinitive=infinitive)
        except ObjectDoesNotExist:
            verb = verbs_models.Verb()
        verb.infinitive = infinitive
        verb.simple_past = simple_past
        verb.past_participle = past_participle
        verb.save()

    def handle(self, *args, **options):
        with open(options['csv_file'], 'rb') as csvfile:
            for verbs in csv.reader(csvfile, delimiter=','):
                self.create_verb(verbs)
