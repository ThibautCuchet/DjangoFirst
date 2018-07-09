# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):

    return HttpResponse("""
        <h1>Bienvenue sur ce site</h1>
        <h2>Pour le moment c est un test</h2>
    """)


def view_article(request, id_article):

    return HttpResponse("""
        <h1>Voici l'article {0} </h1>
    """.format(id_article))

