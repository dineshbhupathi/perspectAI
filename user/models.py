# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # USER_TYPE_CHOICES = (
    #     (1, 'admin'),
    #     (2, 'hr'),
    # )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    def __str__(self):
        if self.user.username == None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return self.user.username

class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    emp_salary = models.FloatField()
    hr = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name