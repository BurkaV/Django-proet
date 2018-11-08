from django.db import models

class Articles(models.Model):
	title = models.CharField(max_length = 120)
	post = models.TextField()
	data = models.DateTimeField()

	def _str_(self):
		return self.title
		