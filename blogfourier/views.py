# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.utils import timezone
from .models import blogs

# Create your views here.


def post_list(request):
    # creation de notre queryset , qui servira a afficher la date de publication (posts)
    posts = blogs.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blogfourier/post_list.html', {'posts': posts})