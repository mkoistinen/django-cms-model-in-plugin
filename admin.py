# -*- coding: utf-8 -*-

from django.contrib import admin

from cms.admin.placeholderadmin import PlaceholderAdmin

from .models import Person


class PersonAdmin(PlaceholderAdmin):
    pass

admin.site.register(Person, PersonAdmin)