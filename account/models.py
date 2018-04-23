from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	'''
	username
	password
	first_name
	last_name
	# are those 4 above necessary since they are otherwise stored?  Or is it a foreign key????
	email
	house_number
	street_name
	town_name
	postcode
	'''