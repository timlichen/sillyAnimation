from django.shortcuts import render, redirect

from models import User, Snack
# Create your views here.
def snack_request(request, id):
	print request.POST['snack_request']
		# user_snack = Snack.SnackManager.snack_request(request.POST['snack_request'])
	return redirect('/index.html')
