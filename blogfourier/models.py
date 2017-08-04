# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
# Create your models here.


class blogs(models.Model):
    author = models.ForeignKey('auth.User', verbose_name='Autheur')
    title = models.CharField(max_length=200, verbose_name='Titre')
    test = models.TextField(verbose_name='Texte')
    create_date = models.DateTimeField(auto_now=True, verbose_name='Date de creation')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Date de Publication')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
