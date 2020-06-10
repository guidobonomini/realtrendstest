from django.urls import path

from rtmeli.accounts.views import (
    login_view,
    logout_view,
    authorize_view,
    signout_view
)

app_name = "accounts"
urlpatterns = [
    path("login/", view=login_view, name="login"),
    path("logout/", view=logout_view, name="logout"),
    path("signout/", view=signout_view, name="signout"),
    path("authorize/", view=authorize_view, name="authorize"),
]
