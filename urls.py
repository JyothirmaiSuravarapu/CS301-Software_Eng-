"""ticketing_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ticketing.views import event_list,buy_ticket,submit_ticket,ticket_success

urlpatterns = [
    path("admin/", admin.site.urls),
    path("events/",event_list),
    path("buy_ticket/",buy_ticket),
    path("submit_ticket/",submit_ticket),
    path("Success/",ticket_success)
]
