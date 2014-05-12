from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^show/(?P<message_id>\d+)/$', 'messages.views.show_message'),
	url(r'^delete/(?P<message_id>\d+)/$', 'messages.views.delete_message'),
	
)

