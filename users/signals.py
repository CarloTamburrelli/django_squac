from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings
from .models import Profile
import os
import logging

logging.basicConfig(level=logging.INFO) # Here


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
		if created:
			prof = Profile.objects.create(user=instance)
			dirtocreate = os.path.join(settings.MEDIA_ROOT+"/profile_pics", str(prof.user.id))
			if os.path.isfile(dirtocreate):
				os.makedirs(dirtocreate)


@receiver(pre_save, sender=Profile)
def auto_delete_file_on_change(sender, instance, **kwargs):

	    if not instance.pk:
	        return False

	    '''try:
	        old_file = Profile.objects.get(pk=instance.pk).image
	    except Profile.DoesNotExist:
	        return False
	    if old_file != 'default.jpg':
		    new_file = instance.image
		    if not old_file == new_file:
		        if os.path.isfile(old_file.path) '''