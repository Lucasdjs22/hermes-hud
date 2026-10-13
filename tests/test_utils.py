"""Regression tests for collector utility helpers."""

import math

import pytest

from hermes_hud.collectors.utils import parse_timestamp


@pytest.mark.parametrize("value", [math.inf, -math.inf, "1e9999", "-1e9999", "", "∞"])
def test_parse_timestamp_returns_none_for_unrepresentable_or_invalid_values(value):
    """Invalid documented timestamp inputs must not leak conversion exceptions."""
    assert parse_timestamp(value) is None
