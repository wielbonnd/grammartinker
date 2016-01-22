import json
from django.views.generic import TemplateView, View
from django.views.generic.base import TemplateResponseMixin
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from apps.profiles import models as profiles_models
from apps.verbs import models as verbs_models
import models


class Menu(TemplateView):
    template_name = "responses/menu.html"

    def get_context_data(self, **kwargs):
        context = super(Menu, self).get_context_data(**kwargs)
        profile_id = kwargs.get('profile_id', 0)
        context['profile'] = get_object_or_404(profiles_models.Profile, pk=profile_id)
        return context


class StartExercise(TemplateResponseMixin, View):
    template_name = "responses/start_exercise.html"

    def get_profile(self, kwargs):
        profile_id = kwargs.get('profile_id', 0)
        profile = get_object_or_404(profiles_models.Profile, pk=profile_id)
        return profile

    def create_Response_session(self, profile):
        session = models.ResponseSession()
        session.profile = profile
        session.save()
        return session

    def get(self, request, *args, **kwargs):
        profile = self.get_profile(kwargs)
        response_session = self.create_Response_session(profile)
        context = {}
        context['profile'] = profile
        context['response_session'] = response_session
        return self.render_to_response(context)


class SaveResponse(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SaveResponse, self).dispatch(request, *args, **kwargs)

    def get_data_from_request(self, request):
        request_data = json.loads(request.body)
        data = {}
        data['response_session_id'] = request_data.get('response_session_id', 0)
        for attr in ['simple_past', 'simple_past_correct',
                     'past_participle', 'past_participle_correct']:
            data[attr] = request_data.get(attr, '')
        return data

    def save_response(self, session, verb, response_data):
        response = models.VerbResponse()
        response.session = session
        response.verb = verb
        for attr in ['simple_past', 'simple_past_correct',
                     'past_participle', 'past_participle_correct']:
            setattr(response, attr, response_data[attr])
        response.save()

    def post(self, request, **kwargs):
        response_data = self.get_data_from_request(request)
        response_session = get_object_or_404(
            models.ResponseSession,
            pk=response_data['response_session_id']
        )
        verb = get_object_or_404(verbs_models.Verb, infinitive=response_data['infinitive'])
        self.save_response(response_session, verb, response_data)
        return JsonResponse("OK")


class ResponsesSession(TemplateView):
    template_name = "responses/responses_sessions_list.html"

    def get_context_data(self, **kwargs):
        context = super(Menu, self).get_context_data(**kwargs)
        profile_id = kwargs.get('profile_id', 0)
        profile = get_object_or_404(profiles_models.Profile, pk=profile_id)
        context['responses_sessions'] = models.ResponseSession.objects.filter(profile=profile)
        return context


class ResponseSessionSummary(TemplateView):
    template_name = "responses/summary.html"

    def get_context_data(self, **kwargs):
        context = super(ResponseSessionSummary, self).get_context_data(**kwargs)
        response_session_id = kwargs.get('response_session_id', 0)
        response_session = get_object_or_404(models.ResponseSession, pk=response_session_id)
        context['response_session'] = response_session
        context['results'] = response_session.get_results()
        return context
