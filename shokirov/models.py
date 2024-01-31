from django.contrib.auth.models import User
from django.db import models


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(AbstractBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def str(self):
        return self.user.username


class Post(AbstractBaseModel):
    title = models.CharField(max_length=128, default="title")
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="usercha")

    def str(self):
        return self.user
