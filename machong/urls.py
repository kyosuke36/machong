from django.urls import path
from . import views

app_name = "machong"

urlpatterns = [
    path("matching/", views.matching, name="matching"),
    path("user/", views.user, name="user"),
    path("settings/<int:user_id>", views.settings, name="settings"),
    path("settings/<int:user_id>/update", views.update, name="update"),
    path("home/<int:user_id>/", views.home, name="home"),
    path("create/", views.create, name="create"),
]
