from django.db import models
from django.utils import timezone

class EName(models.Model):
	Name = models.CharField(max_length=20, help_text='Enter your name')
	entry_date = models.DateField(default=timezone.now())
	
	class Meta:
		ordering = ['-Name']
	def __str__(self):
		return self.Name