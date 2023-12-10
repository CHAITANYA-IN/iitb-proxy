from django.core.mail.message import make_msgid
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from sso import settings

from account_handler.models import UserProfile
from core.utils import DEGREES, HOSTELS, SEXES, SORTED_DISCIPLINES, TabNav
import requests
import jwt


class IndexView(TemplateView):
    template_name = 'sso/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.user.is_authenticated:
            context['base_template'] = 'sso/logged_in.html'
        else:
            context['base_template'] = 'sso/root.html'

        return self.render_to_response(context)


tabs_list = [
    ('basic', 'Basic', 'basic.html'),
    ('api', 'APIs', 'api.html'),
    ('widgets', 'Widgets', 'widget.html'),
    ('best-practices', 'Best Practices', 'practices.html'),
    ('libraries', 'Libraries', 'library.html'),
    ('policy', 'Policy', 'policy.html'),
]


class DocView(TemplateView):
    template_name = 'sso/5-minutes-doc.html'
    tabs = [TabNav(tab[0], tab[1], tab[2], 'doc', tab[0] == 'basic')
            for tab in tabs_list]

    def get_context_data(self, **kwargs):
        context = super(DocView, self).get_context_data(**kwargs)
        context['login_js_url'] = 'https://localhost/static/widget/js/login.min.js'
        context['Message_ID'] = make_msgid()
        context['SORTED_DISCIPLINES'] = SORTED_DISCIPLINES
        context['DEGREES'] = DEGREES
        context['HOSTELS'] = HOSTELS
        context['SEXES'] = SEXES
        context['USER_TYPES'] = UserProfile.objects.values_list(
            'type').distinct()

        # Mark all tabs as inactive
        for tab_ in self.tabs:
            tab_.is_active = False

        tab = context.get('tab', '')
        for tab_ in self.tabs:
            if tab == tab_.tab_name:
                tab = tab_
                break
        else:
            tab = self.tabs[0]
        tab.is_active = True
        context['tabs'] = self.tabs
        context['active_tab'] = tab
        return context

def authorize(request):
    # Redirect users to the OIDC provider's authorization endpoint
    # Update with your OIDC provider's URL
    authorization_url = f'{settings.USSO_BASE}/authorize/'
    redirect_uri = settings.OIDC_CODE_TOKEN_EXCHANGE_URI
    params = {
        'response_type': 'code',
        'client_id': settings.OIDC_CLIENT_ID,
        'redirect_uri': redirect_uri,
        'scope': settings.OIDC_SCOPE,  # Adjust scopes as needed
        'nonce': "hQcplv-NwtyqmhDMLHOnmIFeCXXgipjcXtiF7SnQD8k",
        'state': "WWzLZBJzT0JbKW6vxKpxB19Fi7I",
    }
    redirect_url = f'{authorization_url}?{"&".join(f"{k}={v}" for k, v in params.items())}'
    return redirect(redirect_url)


def token_exchange(request):
    # Obtain an access token from the OIDC provider using the authorization code
    # Update with your OIDC provider's URL
    token_url = f'{settings.USSO_BASE}/token/'
    code = request.GET.get('code')
    state = request.GET.get('state')
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': settings.OIDC_CLIENT_ID,
        'client_secret': settings.OIDC_CLIENT_SECRET,
        'redirect_uri': settings.OIDC_CODE_TOKEN_EXCHANGE_URI,
        'state': state,
    }
    print(request.GET)
    response = requests.post(token_url, data=data)
    print(response.json())
    token_data = response.json()

    # Use the obtained access token to fetch user information from the OIDC user info endpoint
    # Update with your OIDC provider's URL
    user_info_url = f'{settings.USSO_BASE}/user/'
    headers = {'Authorization': f'Bearer {token_data["access_token"]}'}
    user_info_response = requests.get(user_info_url, headers=headers)
    user_info = user_info_response.json()

    # Handle user information as needed
    # ...

    return redirect(reverse('user:home'))
