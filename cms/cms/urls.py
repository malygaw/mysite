from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^article/', include('articles.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^accounts/', include('userprofile.urls')),
    url(r'^accounts/', include('userprofile.urls')),
    url(r'^messages/', include('messages.urls')),

    url(r'^accounts/login/$', 'cms.views.login', name='login'),
    url(r'^accounts/auth/$', 'cms.views.auth_view'),
    url(r'^accounts/loggedin/$', 'cms.views.loggedin'),
    url(r'^accounts/logout/$', 'cms.views.logout', name='logout'),
    url(r'^accounts/invalid_log/$', 'cms.views.invalid_log'),
    url(r'^accounts/create_user/$', 'cms.views.create_user', name='create_user'),
    url(r'^accounts/create_success/$', 'cms.views.create_success'),

)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
