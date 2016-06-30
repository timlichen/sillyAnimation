"""userdashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns, include
from django.contrib import admin
from apps.login_reg.models import User
from apps.dashboard.models import Event

class UserAdmin(admin.ModelAdmin):
	pass
admin.site.register(User, UserAdmin)
admin.site.register(Event, UserAdmin)

urlpatterns = [
	url(r'^', include('apps.landing.urls')),
	url(r'^login/', include('apps.login_reg.urls')),
	url(r'^dashboard/', include('apps.dashboard.urls')),
    url(r'^user/', include('apps.wall.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^snacks/', include('apps.snacks.urls')),
]



# TO RESET SQL LITE DB -
# INSTALL django-extensions
# in the root folder run python manage.py reset_db
# Then run python manage.py migrate again
