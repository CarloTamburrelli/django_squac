from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from PIL import Image
from .utils import checkImgAndSave

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateBody(forms.ModelForm):
	head_img = forms.ImageField( required = False, label = 'Testa' )
	body_img = forms.ImageField( required = False, label = 'Corpo' )
	arm_l_img = forms.ImageField( required = False, label = 'Braccio sinistro' )
	arm_r_img = forms.ImageField( required = False, label = 'Braccio destro' )
	leg_l_img = forms.ImageField( required = False, label = 'Gamba sinistra' )
	leg_r_img = forms.ImageField( required = False, label = 'Gamba destra' )
	#non devo dare gli stessi nomi!! :D
	class Meta:
		model = Profile
		fields = ['head_img', 'body_img']

	def __init__(self, *args, **kwargs):
			super(ProfileUpdateBody, self).__init__(*args, **kwargs)
			self.fields['head_img'].widget.attrs.update({'class': 'form-control mb-4'})
			self.fields['body_img'].widget.attrs.update({'class': 'form-control mb-4'})
			self.fields['arm_l_img'].widget.attrs.update({'class': 'form-control mb-4'})
			self.fields['arm_r_img'].widget.attrs.update({'class': 'form-control mb-4'})
			self.fields['leg_l_img'].widget.attrs.update({'class': 'form-control mb-4'})
			self.fields['leg_r_img'].widget.attrs.update({'class': 'form-control mb-4'})


	def save(self, commit=True):

		profile = super(ProfileUpdateBody, self).save(commit = True)
		
		form_data = self.cleaned_data

		if commit:
			for key,value in form_data.items():

				if (value):
					res = None
					if key == 'head_img':
						output_size = (80,90)
						res = checkImgAndSave(value, 'head', profile.user.id, output_size)
						if (res):
							profile.head = True
					elif key == 'body_img':
						output_size = (117,235)
						res = checkImgAndSave(value, 'body', profile.user.id, output_size)
						if (res):
							profile.body = True
					elif key ==  'arm_l_img':
						output_size = (98,273)
						res = checkImgAndSave(value, 'arm_l', profile.user.id, output_size)
						if (res):
							profile.arm_l = True
					elif key ==  'arm_r_img':
						output_size = (98,273)
						res = checkImgAndSave(value, 'arm_r', profile.user.id, output_size)
						if (res):
							profile.arm_r = True
					elif key ==  'leg_l_img':
						output_size = (89,288)
						res = checkImgAndSave(value, 'leg_l', profile.user.id, output_size)
						if (res):
							profile.leg_l = True
					elif key ==  'leg_r_img':
						output_size = (89,288)
						res = checkImgAndSave(value, 'leg_r', profile.user.id, output_size)
						if (res):
							profile.leg_r = True
			profile.save()


	def clean(self):
		form_data = self.cleaned_data


		print("CONTROLLO...", form_data)
		'''IMAGE_FILE_TYPES = ['png']

		uploaded_image = self.cleaned_data.get("image",  False)

		extension = str(uploaded_image).split('.')[-1]

		file_type = extension.lower()

		for key,value in form_data.items():

			if (not value):
				print('Non hai caricato '+key)
			else:
				print('Stai caricando...'+key)

			if file_type not in IMAGE_FILE_TYPES:
				 raise ValidationError("File is not image.")
			else: '''

		return form_data



#class ProfileUpdateForm(forms.ModelForm):
	#class Meta:
		#model = Profile