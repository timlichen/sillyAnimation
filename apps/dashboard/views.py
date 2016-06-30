from django.shortcuts import render,redirect
from django.db.models import Q
from ..login_reg.models import User
from ..dashboard.models import Event
import datetime

# Create your views here.
def index(request):
	user = User.userManager.getOne(request.session['id'])
	users = User.userManager.getAll()
	query = request.GET.get("search")

	if query:
		users = users.filter(
			Q(first_name__icontains=query)|
			Q(last_name__icontains=query)|
			Q(email__icontains=query)|
			Q(role__icontains=query)).distinct()

	context = {
		'users' : users,
		'curr_user' : user
	}
	return render(request, 'dashboard/benefits.html', context)

def logout(request):
	request.session.clear()
	return redirect('/')

def events(request):
	return render(request, 'dashboard/events.html', context)

def benefits(request):
	return render(request, 'dashboard/benefits.html')

def community(request):
	return render(request, 'dashboard/community.html')

#render add new user (ADMIN)
def new(request):
	return render(request, 'dashboard/new.html')

# ADD a new user (ADMIN)
def add_new(request):
	if request.method == "POST":
		user_tuple = User.userManager.register(request.POST['first_name'],request.POST['last_name'],request.POST['email'],request.POST['password'],request.POST['conf_password'])
		if user_tuple[0] == False:
			context = {
				'errors' : user_tuple[1].values()
			}
			return render(request, 'dashboard/new.html', context)
		else:
			return redirect('../../dashboard')

#RENDER my profile page
def my_profile(request, user_id):
	context = {
		'user' : User.userManager.getOne(user_id)
	}
	return render(request, 'dashboard/profile.html', context)

# Update Email, First and Last name (for all users)
def update_profile(request, user_id):
	if request.method == "POST":
		user_tuple = User.userManager.update_profile(user_id, request.POST['email'], request.POST['first_name'], request.POST['last_name'])
		if user_tuple[0] == False:
			print user_tuple[1].values()
			context = {
				'errors' : user_tuple[1].values()
			}
			return redirect('../../my_profile/'+ user_id, context)
		else :
			return redirect('/../../dashboard')


# Update Email, First and Last name (ADMIN)
def update_profile_admin(request, user_id):
	if request.method == "POST":
		user_tuple = User.userManager.update_profile_admin(user_id, request.POST['email'], request.POST['first_name'], request.POST['last_name'], request.POST['role'])
		if user_tuple[0] == False:
			print user_tuple[1].values()
			context = {
				'errors' : user_tuple[1].values()
			}
			return redirect('../../my_profile/'+ user_id, context)
		else :
			return redirect('/../../dashboard')


# update password (for all users)
def update_profile_pw(request,user_id):
	if request.method == "POST":
		user_tuple = User.userManager.update_profile_pw(user_id, request.POST['password'], request.POST['conf_password'])
		if user_tuple[0] == False:
			context = {
				'errors' : user_tuple[1].values()
			}
			return redirect('../../my_profile/'+ user_id, context)
		else :
			return redirect('/../../dashboard')

# update description (for all users)
def update_profile_desc(request,user_id):
	User.userManager.update_profile_desc(user_id, request.POST['description'])
	return redirect('/../../dashboard')

# show edit page (ADMIN)
def admin_edit(request, user_id):
	context = {
		'user' : User.userManager.getOne(user_id)
	}
	return render(request, "dashboard/edit.html", context)

# REMOVING a user
def remove(request, user_id):
	User.userManager.remove(user_id)
	return redirect('/../../dashboard')

def show(request, user_id):
	context = {
		'user' : User.userManager.getOne(user_id)
	}
	return render(request, 'dashboard/show.html', context)
