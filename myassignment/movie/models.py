from django.db import models


from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    age = models.TextField (blank=True)
    sex = models.TextField (blank=True)
    hobby = models.TextField (blank=True)

    def __str__(self):
        return self.user.username

