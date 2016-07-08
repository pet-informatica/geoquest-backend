# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^random/$', RandomQuestion.as_view(), name='random_question'),
	url(r'^question/$', QuestionList.as_view(), name='question'),
	url(r'^category/$', CategoryList.as_view(), name='category'),
]