from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, default='')
    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    description = models.TextField(max_length=500, default='')
    post_date = models.DateField(auto_now_add=True)

    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} of '
