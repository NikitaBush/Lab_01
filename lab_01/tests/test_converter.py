import pytest

from toolkit.converter import convert
from toolkit.errors import ToolkitError


def test_length():
    assert convert(1, "km", "m") == 1000


def test_mass():
    assert convert(1500, "g", "KG") == 1.5


def test_temperature():
    assert convert(100, "c", "f") == pytest.approx(212)


def test_different_groups():
    with pytest.raises(ToolkitError):
        convert(1, "m", "kg")


def test_unknown_unit():
    with pytest.raises(ToolkitError):
        convert(1, "mile", "m")


def test_below_absolute_zero():
    with pytest.raises(ToolkitError):
        convert(-300, "c", "k")
