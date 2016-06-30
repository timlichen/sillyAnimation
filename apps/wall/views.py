from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from ..login_reg.models import User
from ..dashboard.models import Event
from models import Message
# Create your views here.
def index(request):
	context={'messages': Message.messageManager.all()}
	return render(request, 'wall/index.html', context)

def post_message(request):
	Message.messageManager.create(message=request.POST['message'], title=request.POST['title'], image=request.POST['image'])
	return redirect(reverse('index'))

def events(request):
	Event.objects.create(details=request.POST['detail'], event_date=request.POST['event_dates'])
	return redirect(reverse('index'))
