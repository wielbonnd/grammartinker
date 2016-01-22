import json
import random
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import models


class VerbsJSON(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(VerbsJSON, self).dispatch(request, *args, **kwargs)

    def verb_2_dict(self, verb):
        verb_dict = {}
        for attr in ['infinitive', 'simple_past', 'past_participle']:
            verb_dict[attr] = getattr(verb, attr)
        return verb_dict

    def get(self, request, **kwargs):
        verbs = []
        for verb in models.Verb.objects.all():
            verbs.append(self.verb_2_dict(verb))
        random.shuffle(verbs)
        return JsonResponse(verbs, safe=False)
