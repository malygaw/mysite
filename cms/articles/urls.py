from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^all/$', 'articles.views.articles', name='articles'),
	url(r'^(?P<article_id>\d+)/$', 'articles.views.article'),
	url(r'^(?P<article_id>\d+)/add_comment/$', 'articles.views.add_comment'),
	url(r'^template/$', 'articles.views.template', name='temp'),

)

