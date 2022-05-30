from django.db import models
from django.urls import reverse


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(null=True, blank=True)
    price = models.FloatField()
    STATE_CHOICES = (
        ('new', 'new'),
        ('used', 'used'),
    )
    state = models.CharField(max_length=4, choices=STATE_CHOICES, default='used')
    description = models.TextField(max_length=500, default='')
    post_date = models.DateField(auto_now_add=True)

    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} of '

    @property
    def imageURL(self):
        try:
            url = self.photo.url
        except:
            url = ''
        return url

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})
