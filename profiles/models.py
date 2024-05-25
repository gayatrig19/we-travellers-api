from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Profile Model with one-to-one relationship
    with the User Model to create a profile
    upon user registration.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=300, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_profile_image_uaa7nl'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Makes sure every time a user is created, a
    signal will trigger a Profile model to be created.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
