from django.contrib import admin
import models


@admin.register(models.Verb)
class VerbAdmin(admin.ModelAdmin):
    list_display = ('infinitive', 'simple_past', 'past_participle')
    search_fields = ('infinitive', )
