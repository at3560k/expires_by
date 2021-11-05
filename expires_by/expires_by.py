"""Main module."""

import os
from datetime import datetime

FORMAT = "%Y%m%d"


def now(timestamp: str = None):
    """
    Compute the date
    """
    override = os.getenv("DATETIME_OVERRIDE")

    if override:
        return datetime.strptime(override, FORMAT)

    if timestamp is None:
        return datetime.now()

    return datetime.strptime(timestamp, FORMAT)
