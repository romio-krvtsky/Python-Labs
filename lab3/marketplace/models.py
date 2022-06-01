from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse


# Create your models here.
class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # Validators should be a list

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=200, default='')
    photo = models.ImageField(null=True, blank=True)
    price = models.FloatField()
    STATE_CHOICES = (
        ('new', 'new'),
        ('used', 'used'),
    )
    state = models.CharField(max_length=4, choices=STATE_CHOICES)
    description = models.TextField(max_length=500, default='')
    post_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} of {self.owner}'

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url

    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.pk})
