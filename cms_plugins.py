# -*- coding: utf-8 -*-

from django.conf import settings

from cms.models import CMSPlugin
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import Person


class PersonListPlugin(CMSPluginBase):
    model = CMSPlugin
    name = 'Person List'
    module = 'Proof of Concept'
    render_template = "poc/_person_list.html"
    # text_enabled = True  # Recommend leaving this unset or False!

    def render(self, context, instance, placeholder):

        context.update({
            'person_list': Person.objects.all(),
            'placeholder': placeholder,
        })
        return context

    def icon_src(self, instance):
        return settings.STATIC_URL + u"poc/plugin_people_list.png"


plugin_pool.register_plugin(PersonListPlugin)
