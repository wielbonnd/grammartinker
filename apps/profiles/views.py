from django.views.generic import TemplateView
import models


class Profiles(TemplateView):
    template_name = "profiles/profiles.html"

    def get_context_data(self, **kwargs):
        context = super(Profiles, self).get_context_data(**kwargs)
        context['profiles'] = models.Profile.objects.all()
        return context
