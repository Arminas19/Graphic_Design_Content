from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class blog(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    intro = models.TextField(max_length=80, null=False, blank=False, default='Intro')
    body = models.TextField(max_length=2000, null=False, blank=False)
    image = models.ImageField(upload_to='blogimages', null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True,
                                          verbose_name="date published")
    date_updated = models.DateTimeField(auto_now=True,
                                        verbose_name="date updated")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return self.title
