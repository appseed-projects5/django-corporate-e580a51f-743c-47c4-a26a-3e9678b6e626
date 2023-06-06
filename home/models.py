# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class User(models.Model):

    #__User_FIELDS__
    email = models.CharField(max_length=255, null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class User Manager(models.Model):

    #__User Manager_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__User Manager_FIELDS__END

    class Meta:
        verbose_name        = _("User Manager")
        verbose_name_plural = _("User Manager")


class Profile(models.Model):

    #__Profile_FIELDS__

    #__Profile_FIELDS__END

    class Meta:
        verbose_name        = _("Profile")
        verbose_name_plural = _("Profile")


class Post(models.Model):

    #__Post_FIELDS__

    #__Post_FIELDS__END

    class Meta:
        verbose_name        = _("Post")
        verbose_name_plural = _("Post")


class Comment(models.Model):

    #__Comment_FIELDS__

    #__Comment_FIELDS__END

    class Meta:
        verbose_name        = _("Comment")
        verbose_name_plural = _("Comment")


class Like(models.Model):

    #__Like_FIELDS__

    #__Like_FIELDS__END

    class Meta:
        verbose_name        = _("Like")
        verbose_name_plural = _("Like")


class Follow(models.Model):

    #__Follow_FIELDS__

    #__Follow_FIELDS__END

    class Meta:
        verbose_name        = _("Follow")
        verbose_name_plural = _("Follow")


class Notification(models.Model):

    #__Notification_FIELDS__

    #__Notification_FIELDS__END

    class Meta:
        verbose_name        = _("Notification")
        verbose_name_plural = _("Notification")



#__MODELS__END
