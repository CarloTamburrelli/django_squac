from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	head = models.BooleanField(default=False)
	body = models.BooleanField(default=False)
	arm_l = models.BooleanField(default=False)
	arm_r = models.BooleanField(default=False)
	leg_l = models.BooleanField(default=False)
	leg_r = models.BooleanField(default=False)

	points = models.IntegerField(default=0)
	life_points = models.IntegerField(default=100)

	def __str__(self):
		return f'{self.user.username} Profile'


	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)