from django.contrib import admin
from django.urls import path
from home.views import welcome, lead

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", welcome, name="welcome"),
    path("lead/", lead, name="lead"),
]
