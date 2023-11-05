from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(default="Default.jpg",
                              upload_to='Services Image')
    descriptions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Services'


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Contacts'
