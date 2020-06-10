from django.shortcuts import render
from django.views.generic import TemplateView
from accounts.services import (
    get_auth_url, 
    authorize, 
    get_access_token
)

class LoginView(TemplateView):
    def get(self,request):
        auth_url = get_auth_url()
        print(auth_url)
        return render(request,'account/login.html',{'auth_url':auth_url})

login_view = LoginView.as_view()

class LogoutView(TemplateView):
    def get(self,request):
        return render(request,'account/logout.html')

logout_view = LogoutView.as_view()

class AuthorizeView(TemplateView):
    def get(self,request):
        if(request.query.get('code')):
            authorize(request.query.get('code'))
        return get_access_token()

authorize_view = AuthorizeView.as_view()