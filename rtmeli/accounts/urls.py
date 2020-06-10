from django.urls import path

from rtmeli.accounts.views import (
    login_view,
    logout_view,
    authorize_view,
)

app_name = "accounts"
urlpatterns = [
    path("login/", view=login_view, name="login"),
    path("logout/", view=logout_view, name="logout"),
    path("authorize", view=authorize_view, name="authorize"),
]
