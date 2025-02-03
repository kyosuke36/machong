from django.shortcuts import render

# Create your views here.

def settings(request):
    return render(request, "machong/settings.html")

def matching(request):
    return render(request, "machong/matching.html")