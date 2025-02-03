from django.urls import path
from . import views

app_name = "money"

urlpatterns = [
    path("matching/", views.matching, name="matching"),
    path("settings/", views.settings, name="settings"),
    
]
