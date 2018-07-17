from django.db import models
import datetime
from django.contrib.auth import get_user_model	
from django.utils import timezone

User = get_user_model()

# Create your models here.

class UserFile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	file = models.FileField()
	created_date = models.DateTimeField(default=timezone.now, blank=True)

	def __str__(self):
		return self.name
