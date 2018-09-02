from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

User = settings.AUTH_USER_MODEL

class Companies(models.Model):

	branch_choices = (
		('-','---SELECT---'),
		('CSE','Computer Science & Engineering'),
		('ECE','Electronics and Communication Engineering'),
		('MECH','Mechanical Engineering'),
		('MME','Metallurgy Engineering'),
		('CHE','Chemical Engineering'),
		('CIVIL','Civil Engineering'),
		('EEE','Electrical and Electronics Engineering'),
		('BIO','Biotechnology'),
	)

	user = models.ForeignKey(User,on_delete=models.CASCADE ,blank = True, null = True)
	name = models.CharField(max_length=32)
	ctc = models.CharField(max_length=32)
	cgpa = models.DecimalField(decimal_places=2,max_digits=4)
	br_allowed = models.CharField(max_length=1000)

	def __str__(self):
		return f'{self.name}'

class Applicants(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE ,blank = True, null = True)
	company = models.ForeignKey(Companies,on_delete=models.CASCADE ,blank = True, null = True)
	name = models.CharField(max_length=32)

	def __str__(self):
		return f'{self.name}'