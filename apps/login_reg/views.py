from django.shortcuts import render, redirect

from models import User
# Create your views here.
def index(request):
	return render(request, 'login_reg/index.html')


def login(request):
	if request.method == "POST":
		user_tuple = User.userManager.login(request.POST['email'], request.POST['password'])
		if user_tuple[0]:
			request.session['id'] = user_tuple[1].id
			request.session['name'] = user_tuple[1].first_name + " " + user_tuple[1].last_name
			request.session['role'] = user_tuple[1].role
			print request.session['name']
			return redirect('../../dashboard/events')
		else:
			context = {
				'errors': user_tuple[1].values()
			}
			return render(request, 'login_reg/index.html', context)


def register(request):
	return render(request, 'login_reg/register.html')

def registering(request):
	if request.method == "POST":
		user_tuple = User.userManager.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'],request.POST['conf_password'])
		if user_tuple[0] == False:
			context = {
				'errors' : user_tuple[1].values()
			}
			return render(request, 'login_reg/register.html', context)
		else:
			print user_tuple[1].id
			request.session['id'] = user_tuple[1].id
			request.session['name'] = user_tuple[1].first_name + " " + user_tuple[1].last_name
			return redirect('../../dashboard')
