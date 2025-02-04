from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.template import loader
from django.shortcuts import reverse
from django.shortcuts import get_object_or_404
from .models import User


def user(request):
    return render(request, "machong/user.html")


def settings(request, user_id):
    template = loader.get_template("machong/settings.html")
    target_user = get_object_or_404(User, id=user_id)
    context = {"target_user": target_user}
    return HttpResponseRedirect(reverse("machong:settings", args=[user_id]))
    return HttpResponse(template.render(context, request),)


def update(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    target_user.name = request.POST.get("user_name")
    target_user.gender = request.POST.get("gender")
    target_user.purpose = request.POST.get("purpose")
    target_user.level = request.POST.get("level")
    target_user.time = request.POST.get("time")
    target_user.email = request.POST.get("email")
    target_user.save()
    return HttpResponseRedirect(reverse("machong:home", args=[user_id]))


def matching(request):
    return render(request, "machong/matching.html")


def create(request):
    name_text = request.POST["user_name"]
    gender_text = request.POST["gender"]
    purpose_text = request.POST["purpose"]
    level_text = request.POST["level"]
    time_text = request.POST["time"]
    email_text = request.POST["email"]

    u = User.objects.create(
        name=name_text,
        gender=gender_text,
        purpose=purpose_text,
        level=level_text,
        time=time_text,
        email=email_text,
    )

    return HttpResponseRedirect(reverse("machong:home", args=[u.id]))


def home(request, user_id):
    template = loader.get_template("machong/home.html")
    target_user = get_object_or_404(User, id=user_id)
    context = {"target_user": target_user, "user_id": user_id}
    return HttpResponse(template.render(context, request))
