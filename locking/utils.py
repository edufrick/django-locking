# encoding: utf-8

from __future__ import absolute_import

from django.contrib.contenttypes.models import ContentType

from locking.models import Lock


def gather_lockable_models():
    lockable_models = dict()
    for contenttype in ContentType.objects.all():
        model = contenttype.model_class()
        # there might be a None value betwixt our content types
        if model:
            app = model._meta.app_label
            name = model._meta.module_name
            if issubclass(model, Lock):
                lockable_models.setdefault(app, {})
                lockable_models[app][name] = model
    return lockable_models
