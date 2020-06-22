# encoding: utf-8

from __future__ import absolute_import

from django.contrib import admin

from locking.admin import LockableAdmin
from locking.tests.models import Story


class StoryAdmin(LockableAdmin):
    list_display = (
        "lock",
        "content",
    )
    list_display_links = ("content",)


admin.site.register(Story, StoryAdmin)
