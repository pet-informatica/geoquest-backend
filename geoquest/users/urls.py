# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^rank/$', RankList.as_view(), name='rank_list'),
	url(r'^statistics/$', StatisticsList.as_view(), name='statistics'),
	url(r'^badges/$', BadgeList.as_view(), name='badges'),
	url(r'^progress/$', Progress.as_view(), name='progress'),
]