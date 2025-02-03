from django.urls import path
from . import views

app_name = "machong"

urlpatterns = [
    path("matching/", views.matching, name="matching"),
    path("settings/", views.settings, name="settings"),
    
]
