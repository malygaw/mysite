#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Messages(models.Model):
	title = models.CharField(max_length=150, verbose_name="Tytuł")
	content = models.TextField(verbose_name="Wiadomość")
	view = models.BooleanField(default=False, verbose_name="Odczytana")
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.title

@receiver(post_save, sender=User)
def welcome_message(sender, **kwargs):
	if kwargs.get('created', False):
		Messages.objects.create(user=kwargs.get('instance'),
			title = "Witaj nowy użytkowniku", 
			content = "Powitanie",
			)
