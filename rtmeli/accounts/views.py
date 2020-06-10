from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from accounts.services import (
    get_auth_url, 
    authorize, 
    get_access_token
)

class LoginView(TemplateView):
    def get(self,request):
        auth_url = get_auth_url()
        return render(request,'account/login.html',{'auth_url':auth_url})

login_view = LoginView.as_view()

class LogoutView(TemplateView):
    def get(self,request):
        return render(request,'account/logout.html')

logout_view = LogoutView.as_view()

class AuthorizeView(TemplateView):
    def get(self,request):
        if(request.GET.get('code')):
            authorize((request.GET.get('code'))
        access_token = get_access_token()
        request.session['access_token'] = access_token
        return HttpResponseRedirect('users:profile')


authorize_view = AuthorizeView.as_view()