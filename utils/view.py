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

import json

from django.conf import settings
from django.template import Context, Engine
from django.http import HttpResponse
from django.views.generic import View

js_catalog_template = r"""
{% autoescape off %}
(function(globals) {
    let django = globals.django || (globals.django = {});

    django.jsSettings = django.jsSettings || {};
      {% if JsSettings %}
    var jsConfigs = {{ JsSettings }};
    for (var key in jsConfigs) {
        django.jsSettings[key] = jsConfigs[key];
    }

    if (!django.jsSettings_initialized) {
        django.getJsConfig = function(attr) {
            var value = django.jsSettings[attr];
            if (typeof(value) == 'undefined') {
                return attr;
            } else {
                return value;
            }
        };

        /* add to global namespace */
        globals.getJsConfig = django.getJsConfig;

        django.jsSettings_initialized = true;
    }
  {% endif %}
}(this));
{% endautoescape %}
"""

js_global_settings = {

}


class JavaScriptSettings(View):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def render_to_response(self, context, **response_kwargs):
        def indent(s):
            return s.replace('\n', '\n  ')

        template = Engine().from_string(js_catalog_template)
        context['JsSettings'] = indent(json.dumps(context['settings'], sort_keys=True, indent=2))
        return HttpResponse(template.render(Context(context)), 'text/javascript; charset="utf-8"')

    def get_settings(self):
        return js_global_settings

    def get_context_data(self, **kwargs):
        return {
            'settings': self.get_settings(),
        }
