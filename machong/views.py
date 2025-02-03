from django.shortcuts import render


def settings(request):
    return render(request, "machong/user.html")


def matching(request):
    return render(request, "machong/matching.html")
