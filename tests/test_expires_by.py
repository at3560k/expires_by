#!/usr/bin/env python

"""Tests for `expires_by` package."""

# import pytest

from datetime import datetime, timedelta


from expires_by import expires_by


def test_is_recent():
    """Sample pytest test function with the pytest fixture as an argument."""
    dt = expires_by.now()
    assert dt <= datetime.now()
    assert dt - timedelta(seconds=1) < datetime.now()
