from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<user_id>\d+)/$', views.index, name="index"),
	url(r'^add_msg/(?P<wall_id>\d+)/$', views.add_msg, name="add_msg"),
	url(r'^add_comment/(?P<msg_id>\d+)/$', views.add_comment, name="add_comment"),


]