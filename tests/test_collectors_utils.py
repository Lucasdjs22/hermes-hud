"""Regression tests for collector parsing helpers."""

import pytest

from hermes_hud.collectors.utils import parse_timestamp


@pytest.mark.parametrize("value", ["1e999", "", "∞"] )
def test_parse_timestamp_invalid_strings_return_none(value):
    """Invalid numeric, empty, and Unicode strings must not escape the helper."""
    assert parse_timestamp(value) is None
