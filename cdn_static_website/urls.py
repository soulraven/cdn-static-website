"""cdn_static_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.views.i18n import JavaScriptCatalog
from django.views.decorators.http import last_modified
from django.conf.urls.i18n import i18n_patterns
from django.utils import timezone


# import Http Response from django
from django.http import HttpResponse
# get datetime
import datetime

admin.autodiscover()


def hello(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = f"Time is {now}"
    # return response
    return HttpResponse(html)


urlpatterns = [
    path('', hello),
    path('admin/', admin.site.urls),
]

js_info_dict = {
    'domain': 'django',
    'packages': getattr(settings, 'PROJECT_APPS'),
}

last_modified_date = timezone.now()
urlpatterns += i18n_patterns(
    path('jsi18n/', last_modified(lambda req, **kw: last_modified_date)(JavaScriptCatalog.as_view(**js_info_dict)),
         name='javascript-catalog')
)
