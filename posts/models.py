from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Post listed in descending order with most recent date:
    created/updated.
    """

    REGION_CHOICES = (
        ('Asia', 'Asia'),
        ('Africa', 'Africa'),
        ('North America', 'North America'),
        ('South America', 'South America'),
        ('Antarctica', 'Antarctica'),
        ('Europe', 'Europe'),
        ('Australia (Oceania)', 'Australia (Oceania)'),
    )

    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_posts_image_cdoz8g',
        blank=True
    )
    place = models.CharField(max_length=150, blank=True)
    region = models.CharField(
        max_length=50,
        choices=REGION_CHOICES,
        default='Europe'
    )
    image_filter = models.CharField(
        max_length=32,
        choices=image_filter_choices,
        default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'