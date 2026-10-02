from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Lead

def welcome(request):
    return render(request, "welcome.html")

def lead(request):
    if request.method == "POST":
        Lead.objects.create(
            name=request.POST.get("name", "").strip(),
            email=request.POST.get("email", "").strip(),
            message=request.POST.get("message", "").strip(),
        )
        messages.success(request, "Lead submitted successfully!")
        return redirect("welcome")
    return redirect("welcome")
