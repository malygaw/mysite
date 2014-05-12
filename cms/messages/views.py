from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import Messages

def show_message(request, message_id):
	m = Messages.objects.get(id=message_id)
	return render_to_response('message.html', {'message': m})

def delete_message(request, message_id):
	m = Messages.objects.get(id=message_id)
	m.view = True
	m.save()
	return HttpResponseRedirect('/accounts/loggedin/')

