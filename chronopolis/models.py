from django.db import models
from django.contrib.auth.models import User

class Survey(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=60)
	instructions = models.CharField(max_length=600)

	def __unicode__(self):
		return self.title

class Question(models.Model):
	TYPE_CHOICES = (
		(1, 'Boolean'),
		(2, 'Integer')
	)

	survey = models.ForeignKey(Survey)
	text = models.CharField(max_length=60)
	type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES)

	def __unicode__(self):
		return self.text
