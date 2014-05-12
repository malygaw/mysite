from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from messages.models import Messages

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/accounts/loggedin/')
	else:
		return HttpResponseRedirect('/accounts/invalid_log/')

def loggedin(request):
	m = Messages.objects.filter(user=request.user, view=False)
	return render_to_response('loggedin.html', {'user_name': request.user.username, 'messages': m})

def invalid_log(request):
	return render_to_response('invalid_log.html')

@login_required
def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

def create_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/create_success/')

	args = {}
	args.update(csrf(request))
	args['form'] = UserCreationForm()

	return render_to_response('create_user.html', args)

def create_success(request):
	return render_to_response('create_success.html')