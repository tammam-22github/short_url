from django.urls import path
from short_url.views import *

app_name = "short_url"

urlpatterns = [
    path(
        route="",
        view=ShortURlView.as_view(),
        name="short_url_view",
    ),
    path(
        route="short_url/<pk>/",
        view=ShortURLDetailView.as_view(),
        name="detail_url",
    ),
    path(
        route="redirect/<str:short_url>",
        view=RedirectToUrl.as_view(),
        name="rediret_to_url",
    ),
]
