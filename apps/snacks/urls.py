from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^snack_request/(?P<id>\d+)/$',views.snack_request, name="snack_request"),
]
