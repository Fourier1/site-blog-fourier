# -*- coding: utf-8 -*-

from django.contrib import admin
from blogfourier.models import blogs
# Register your models here.

# importer le model sur l'interface de l'admin
admin.site.register(blogs)
