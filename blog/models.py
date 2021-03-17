from django.db import models

class Contact(models.Model):
	name = models.CharField(max_length = 50)
	surname = models.CharField(max_length = 50)
	date = models.CharField(max_length = 20)
	tel_number = models.CharField(max_length = 30)

	def __str__(self):
		return self.name