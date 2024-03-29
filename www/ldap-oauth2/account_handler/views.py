from django.db.models.signals import pre_save
import logging
import requests
import base64
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.models import User
from account_handler.models import UserProfile
from django.utils.http import urlencode
from django.urls import set_script_prefix

from core.mixins import SensitivePostParametersMixin

from .forms import LoginForm

try:
    from urllib.parse import quote_plus
except ImportError:
    from urllib import quote_plus

logger = logging.getLogger(__name__)


class LoginView(SensitivePostParametersMixin, View):
    """
    GET: If user is already logged in then redirect to 'next' parameter in query_params
        Else render the login form
    POST:
        Validate form, login user
    """
    form_class = LoginForm
    template_name = 'account/login.html'

    def get(self, request):
        if not request.META['SCRIPT_NAME']:
            set_script_prefix('/')

        uhome = request.build_absolute_uri(
            reverse('user:home'))  # http://localhost:8000/user/
        endpoint = uhome # + 'redir'  # http://localhost:8000/user/redir
        current_url = request.resolver_match.url_name  # login

        context = {
            'form': self.form_class,
            'usso_url': request.build_absolute_uri(reverse('oidc_authentication_init')), # endpoint + '?' + urlencode({'logout': request.build_absolute_uri(uhome)}),
            'usso_base': settings.USSO_BASE,
            'usso_widget': settings.USSO_RU,
        }
        for i, j in context.items():
            print(f'{i}: {j}')
            logger.debug('GET /login context: %s', f'{i}: {j}')

        return render(request, self.template_name, context)

    def post(self, request):
        next_ = request.GET.get('next', settings.LOGIN_REDIRECT_URL)
        logger.debug('POST next: %s', next_)
        return redirect(next_)


class LogoutView(View):
    def get(self, request):
        logger.debug('GET request: %s', request)
        logout(request)
        logger.debug('Logged user out')
        usso_redir = reverse('user:home') + '?' # 'redir?'
        logger.debug('GET usso_redir: %s', usso_redir)
        next_ = request.GET.get('next')
        login_url = reverse('account:login')
        redirect_to = login_url

        if next_ is not None:
            next_ = quote_plus(next_)
            redirect_to = '%s?next=%s' % (
                login_url, next_) if next_ else login_url

        logger.debug('GET next: %s', next_)
        logger.debug('GET redirect_to: %s', redirect_to)

        if settings.USSO_RU:
            return HttpResponseRedirect(usso_redir + urlencode({'logout': request.build_absolute_uri(redirect_to)}))

        return HttpResponseRedirect(redirect_to)


def user_save(sender, instance, *args, **kwargs):
    instance.last_name = instance.last_name[:28]
    instance.first_name = instance.first_name[:28]


pre_save.connect(user_save, sender=User)
