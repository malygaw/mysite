#-*- coding: utf-8 -*-
from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=150, verbose_name="Tytuł")
	content = models.TextField(verbose_name="Treść")
	published = models.DateTimeField(verbose_name="Data publikacji")
	image = models.FileField(upload_to="images/", verbose_name="Obraz")

	def __unicode__(self):
		return self.title


class Comment(models.Model):
	name = models.CharField(max_length=150, verbose_name="Użytkownik")
	content = models.TextField(verbose_name="Komentarz")
	published = models.DateTimeField(verbose_name="Data publikacji")
	article = models.ForeignKey(Article)

	def __unicode__(self):
		return self.name

