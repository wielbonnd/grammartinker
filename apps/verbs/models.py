from django.db import models


class LowerChartFiled(models.CharField):

    def to_python(self, value):
        value = super(LowerChartFiled, self).to_python(value)
        return value.lower()


class Verb(models.Model):
    infinitive = LowerChartFiled(
        max_length=32,
        unique=True
    )
    simple_past = LowerChartFiled(
        max_length=32
    )
    past_participle = LowerChartFiled(
        max_length=32
    )

    def __unicode__(self):
        return self.infinitive.capitalize()
