from django.db import models
from django.db.models.functions import Coalesce


class ResponseSession(models.Model):
    profile = models.ForeignKey(
        'profiles.Profile'
    )
    date = models.DateTimeField(
        auto_now_add=True
    )

    def get_results(self):
        # TODO :move this to manager
        results = self.verbs.aggregate(
            simple_past_correct=Coalesce(models.Sum(
                models.Case(
                    models.When(simple_past_correct=True, then=1),
                    output_field=models.IntegerField()
                )
            ), models.Value(0)),
            past_participle_correct=Coalesce(models.Sum(
                models.Case(
                    models.When(past_participle_correct=True, then=1),
                    output_field=models.IntegerField()
                )
            ), models.Value(0)),
            all=models.Count('pk')
        )
        results['summary'] = results['simple_past_correct'] + results['past_participle_correct']
        results['all2'] = results['all'] * 2
        return results

    def __unicode__(self):
        return u'{} {}'.format(self.profile, self.date)


class VerbResponse(models.Model):
    session = models.ForeignKey(
        ResponseSession,
        related_name='verbs'
    )
    verb = models.ForeignKey(
        'verbs.Verb'
    )
    simple_past = models.CharField(
        max_length=32
    )
    simple_past_correct = models.BooleanField(
    )
    past_participle = models.CharField(
        max_length=32
    )
    past_participle_correct = models.BooleanField(
    )
