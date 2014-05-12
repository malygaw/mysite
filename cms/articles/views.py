from django.shortcuts import render_to_response
from articles.models import Article, Comment
from forms import FormComment
from django.core.context_processors import csrf
from django.utils import timezone
from django.http import HttpResponseRedirect

def articles(request):
	return render_to_response('articles.html', {'articles' : Article.objects.all()})

def article(request, article_id):
	return render_to_response('article.html',{'article' : Article.objects.get(id=article_id)})

def add_comment(request, article_id):
	art = Article.objects.get(id=article_id)

	if request.method == "POST":
		fc = FormComment(request.POST)
		if fc.is_valid():
			comment = fc.save(commit=False)
			comment.published = timezone.now()
			comment.article = art
			comment.save()

			return HttpResponseRedirect('/article/%s' % article_id)

	else:
		fc = FormComment()

	args = {}
	args.update(csrf(request))
	args['article'] = art
	args['form'] = fc

	return render_to_response('add_comment.html', args)

def template(request):
	return render_to_response('template.html')