from __future__ import absolute_import

import logging

from django.conf import settings

VERSION = (0, 3, 5)

# TODO: LOCK_TIMEOUT isn't being used anymore, clean it up throughout the code
LOCK_TIMEOUT = getattr(settings, "LOCK_TIMEOUT", 1800)

logger = logging.getLogger("django.locker")

time_until_expiration = int(settings.LOCKING["time_until_expiration"])
time_until_warning = settings.LOCKING["time_until_warning"]
