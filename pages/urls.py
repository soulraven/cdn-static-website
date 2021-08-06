#  -*- coding: utf-8 -*-
#
#              Copyright (C) 2018-2021 ProGeek
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.urls import path, include
from django.views.decorators.http import last_modified
from django.utils import timezone

from .views import IndexView, AboutView
from utils.view import JavaScriptSettings

last_modified_date = timezone.now()

app_name = 'pages'
urlpatterns = [
    path('', IndexView.as_view(), name='index-page'),
    path('about', AboutView.as_view(), name='about-page'),
    path('js_settings/', last_modified(lambda req, **kw: last_modified_date)(JavaScriptSettings.as_view()),
         name='javascript-settings')
]
