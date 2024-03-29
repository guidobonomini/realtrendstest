from django.urls import path

from rtmeli.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    profile_view
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("profile/", view=profile_view, name="profile"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
