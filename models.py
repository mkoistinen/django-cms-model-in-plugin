# -*- coding: utf-8 -*-

from django.db import models
from cms.models.fields import PlaceholderField


class Person(models.Model):
    class Meta:
        app_label = "poc"

    name = models.CharField('name', max_length=32, blank=False, default="")
    title = models.CharField('title', max_length=32, blank=False, default="")
    bio = PlaceholderField('person_bio')

    def __unicode__(self):
        return self.name

    #
    # Purpose of this save() override:
    # =========================================================================
    # We just want to ensure that a TextPlugin is added to the placeholder on
    # INITIAL save only. This is to work around a design-flaw in django-cms
    # 3.0.0beta3 (https://github.com/divio/django- cms/issues/2433) where
    # PlaceholderFields that are presented via CMSPlugins are not create-able
    # since the "structure" mode of the CMSPlugin reveals none of its content,
    # and therefore, there is no way to ADD content to the placeholder.
    #
    # If there is already content there, however, it can be edited in the
    # "content mode" by hovering over the existing content and double-
    # clicking.
    #

    def save(self, *args, **kwargs):
        from cms.api import add_plugin

        if not self.pk:
            super(Person, self).save(*args, **kwargs) # Call the "real" save() method.
            add_plugin(self.bio, 'TextPlugin', 'en', body="<p>Biography coming soon.</p>")
        else:
            super(Person, self).save(*args, **kwargs) # Call the "real" save() method.

