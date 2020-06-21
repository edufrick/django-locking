from __future__ import absolute_import

import datetime

from django.db.models import Manager
from django.db.models import Q

from locking import LOCK_TIMEOUT


"""
    LOCKED
            if (datetime.today() - self.locked_at).seconds < LOCK_TIMEOUT:


            self.locked_at < (NOW - TIMEOUT)
"""


def point_of_timeout():
    delta = datetime.timedelta(seconds=LOCK_TIMEOUT)
    return datetime.datetime.now() - delta


class LockedManager(Manager):
    def get_query_set(self):
        timeout = point_of_timeout()
        return (
            super(LockedManager, self)
            .get_query_set()
            .filter(_locked_at__gt=timeout, _locked_at__isnull=False)
        )


class UnlockedManager(Manager):
    def get_query_set(self):
        timeout = point_of_timeout()
        return (
            super(UnlockedManager, self)
            .get_query_set()
            .filter(Q(_locked_at__lte=timeout) | Q(_locked_at__isnull=True))
        )
