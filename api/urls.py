#!/usr/bin/env python
# encoding: utf-8
'''
@author:imuzcy
@file: urls.py
@time: 2021/4/3 18:36
@contact: chenyangzhou19940217@gmail.com
'''

from django.urls import path
from api import views

urlpatterns = [
    path('submit/', views.SubmitView.as_view()),
]