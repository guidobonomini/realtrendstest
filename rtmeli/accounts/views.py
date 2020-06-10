from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, RedirectView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

from ..api.services import MercadolibreApi

from accounts.services import (
    get_auth_url, 
)

from utils.decorators import login_required

class LoginView(TemplateView):
    def get(self,request):
        auth_url = get_auth_url()
        return render(request,'account/login.html',{'auth_url':auth_url})

login_view = LoginView.as_view()

class LogoutView(TemplateView):
    @method_decorator(login_required())
    def get(self,request):
        return render(request,'account/logout.html')

logout_view = LogoutView.as_view()

class SignoutView(RedirectView):
    @method_decorator(login_required())
    def get(self,request):
        #TODO: change logout behaviour to work with allauth
        del request.session['access_token']
        request.session.modified = True
        return HttpResponseRedirect(reverse('home'))

signout_view = SignoutView.as_view()

class AuthorizeView(TemplateView):
    def get(self,request):
        if(request.GET.get('code')):
            token = get_access_token(request.GET.get('code'))
        request.session['access_token'] = token
        request.session.modified = True
        return HttpResponseRedirect(reverse('home'))

authorize_view = AuthorizeView.as_view()