from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Usuario

@receiver(post_save, sender=Usuario)
def create_auth_user(sender, instance, created, **kwargs):
    if created and not User.objects.filter(username=instance.form_user).exists():
        user = User.objects.create_user(username=instance.form_user, password=instance.form_password)
        user.email = instance.form_correo
        user.first_name = instance.form_user
        user.save()