"""logint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from account.views import (
    register_view,
    home,
    login_view,
    logout_view,
    details,
    vendor_reg,
    get_latlon,
    profile_update,
    vendor_profile

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name="register"),
    path('', home, name="home"),
    path('profile/', profile_update, name="profile"),
    path('vendor_regestration/', vendor_reg, name='vendor-regestration'),
    path('details/', details, name="details"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('lat/', get_latlon, name="get_latlon"),
    path('vendor_profile/', vendor_profile, name="vendor_profile"),
]
