from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm ,ProfileUpdateBody 
from .models import Profile
from django.conf import settings
from django.contrib.auth.models import Group



def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			group = Group.objects.get(name = 'gamer')
			user.groups.add(group)
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account creato! Adesso puoi loggarti {username}!')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', { 'form' : form })


@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateBody(request.POST, request.FILES,  instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Account aggiornato!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateBody()

	context = {
		'u_form' : u_form,
		'p_form' : p_form
	}

	return render(request, 'users/profile.html', context)