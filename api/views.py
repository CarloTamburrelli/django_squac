from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from PIL import Image
from django.db.models import Q

from django.utils import timezone
import os

from users.models import Profile
from system.models import SystemGame

@api_view(['GET'])
@login_required
def clickMatrix(request, matrix):
	try:
		profile = Profile.objects.get(user_id=request.user.id)
	except Profile.DoesNotExist:
		profile = None
	flag = 0
	if (profile):
		profile.points = profile.points + 1
		profile.save()

		try:
			fightToCombat = SystemGame.objects.get(~Q(step = 3), ~Q(user2_id = None), Q(user1_id=profile.user_id) | Q(user2_id=profile.user_id))
		except SystemGame.DoesNotExist:
			fightToCombat = None


		if (fightToCombat):
			if (fightToCombat.step == 2):
				#devo solo darti i risultati a video (con modal)
				#imposto qui step+1?
				api_results = {
					'status' : 1,
					'points' : profile.points,
				}

				return Response(api_results)

			elif ((fightToCombat.user1_id == profile.user_id) and (not fightToCombat.user1_finish)):
				#non hai ancora giocato e sono il primo
				api_results = {
					'status' : 1,
					'points' : profile.points,
					'go_to_fight' : 1,
					'fight_id' : fightToCombat.id,
				}

				return Response(api_results)

			elif ((fightToCombat.user2_id == profile.user_id) and (not fightToCombat.user2_finish)):
				#non hai ancora giocato e sono il secondo
				api_results = {
					'status' : 1,
					'points' : profile.points,
					'go_to_fight' : 1,
					'fight_id' : fightToCombat.id,
				}

				return Response(api_results)

			elif (fightToCombat.matrix_id == str(matrix)):
				#ho giocato ma l'altro giocatore no, ma continua a essere la stessa matrice
				#non posso creare un ulteriore fight per quella matrice, ci sarebbero troppi match in coda
				api_results = {
					'status' : 1,
					'points' : profile.points,
				}

				return Response(api_results)

		try:
			fight = SystemGame.objects.get(matrix_id=str(matrix), user2_id = None)
		except SystemGame.DoesNotExist:
			fight = None

		if (fight): #cerca solo quelli che non hanno ancora un compagno nella battaglia

			intervallo = (timezone.now() - timezone.timedelta(minutes=1)) 
			game_date = (fight.game_date)

				#se entro un minuto qualcun'altro schiccia lo stesso quadrato nella stessa posizione

			if (((intervallo) < game_date) and (fight.user1_id != profile.user_id)):
				fight.user2_id = request.user.id
				fight.save()
			else:
				#rimpiazza combattimento, perche' quella battaglia e' ormai vecchia
				fight.delete()
				newfight = SystemGame.objects.create(user1_id = request.user.id, matrix_id = str(matrix))
				newfight.save()



		else:
			fight = SystemGame.objects.create(user1_id = request.user.id, matrix_id = str(matrix))
			fight.save()


		flag = 1
	
		
	api_results = {
		'status' : flag,
		'points' : profile.points,
	}

	return Response(api_results)



@api_view(['GET'])
@login_required
def removeBodyPart(request, partbody):

	profile = Profile.objects.get(user_id=request.user.id)
	flag = 0

	if profile:
		path = 'media/profile_pics/'+str(request.user.id)+'/'+partbody+'.png'
		if os.path.isfile(path):
		    os.remove(path)
		setattr(profile, partbody, 0)
		profile.save()
		flag = 1
		
	api_results = {
		'status' : flag,
	}

	return Response(api_results)



@api_view(['GET'])
def userList(request):
	users = User.objects.all()
	serializer = UserSerializer(users, many=True)
	return Response(serializer.data)


'''
#esempio di CREATE
@api_view(['POST'])
def taskInsert(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data) '''


'''
#esempio di UPDATE
@api_view(['POST'])
def taskUPDATE(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)
	
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data) '''

'''
#esempio di DELETE
@api_view(['GET'])
def taskUPDATE(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()
		
	return Response("ITEM RIMOSSO!") '''


@api_view(['GET'])
def userDetail(request, pk):
	users = User.objects.get(id=pk)
	serializer = UserSerializer(users, many=False)
	return Response(serializer.data)