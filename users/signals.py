from django.apps import apps
from django.core.mail import send_mail
from django.db.models.signals import post_save, post_delete
from django.conf import settings 
from django.dispatch import receiver 

Profile = apps.get_model('bookreview', 'Profile')

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def createProfile(sender, instance, created, **kwargs):
    '''Creates profile when use is created
       Sends welcome email to the email of created user. '''
    Profile = apps.get_model('bookreview', 'Profile')
    subject = 'Welcome to ReadReels'
    message = 'You are registered in readreels. Thank you'

    if created: 
        user = instance
        profile = Profile.objects.create(
            user = instance,
        )

    send_mail (
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [profile.user.email],
        fail_silently=False
    )


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    '''Deletes user when the associated profile is deleted'''
    user = instance.user
    user.delete()