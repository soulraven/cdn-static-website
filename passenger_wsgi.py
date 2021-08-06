
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

import os
import sys

cwd = os.getcwd()

env_workzone_path = os.environ.get('WORKZONE_PATH', '/opt/workzone')
workzone_path = os.path.abspath(env_workzone_path)

assert os.path.exists(workzone_path), "Workzone path is not valid"

# smart guessing that the virtualenvs is in the correct place
virtualenvs_path = os.path.join(workzone_path, '.virtualenvs')

INTERP = os.path.join(virtualenvs_path, os.path.basename(cwd), 'bin', 'python3')
# INTERP is present twice so that the new python interpreter
# knows the actual executable path
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# from this point we can use the packages from the virtual environment

sys.path.append(cwd)
sys.path.append(os.path.join(cwd, 'cdn_static_website'))  # You must add your project here

sys.path.insert(0, os.path.join(virtualenvs_path, 'cdn-static-website', 'bin'))
sys.path.insert(0, os.path.join(virtualenvs_path, 'cdn-static-website', 'lib', 'python3.9', 'site-packages'))

os.environ['DJANGO_SETTINGS_MODULE'] = "cdn_static_website.settings"
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
