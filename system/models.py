from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class SystemGame(models.Model):
	user1 = models.ForeignKey(User, null=True, related_name='utente1', on_delete=models.SET_NULL)
	user2 = models.ForeignKey(User, null=True, related_name='utente2', on_delete=models.SET_NULL)
	user1_finish = models.BooleanField(default=False)
	user2_finish = models.BooleanField(default=False)
	user1_points = models.IntegerField(default=0)
	user2_points = models.IntegerField(default=0)
	user1_bonus_points = models.IntegerField(default=0)
	user2_bonus_points = models.IntegerField(default=0)
	game_date = models.DateTimeField(default=timezone.now)
	matrix_id = models.CharField(max_length=10)
	step = models.PositiveSmallIntegerField(default=0) #quando step e' uguale a 2 il gioco e' terminato


	def __str__ (self):
		return "Gioco con id "+str(self.id)

	class Meta:
		db_table = "system_game"



'''
	
'''
	