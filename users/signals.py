from django.apps import apps
from django.db.models.signals import post_save
from django.conf import settings 
from django.dispatch import receiver

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createProfile(sender, instance, created, **kwargs):
    Profile = apps.get_model('bookreview', 'Profile')
    if created: 
        user = instance
        profile = Profile.objects.create(
            user = instance,
        )