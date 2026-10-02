import pytest

from toolkit.calculator import evaluate
from toolkit.errors import ToolkitError


def test_add_and_subtract():
    assert evaluate("2 + 3") == 5
    assert evaluate("10 - 4 - 3") == 3


def test_multiply_and_divide():
    assert evaluate("6 * 7") == 42
    assert evaluate("10 / 4") == 2.5


def test_precedence():
    assert evaluate("2 + 3 * 4") == 14
    assert evaluate("7 + 8 / 4 - 1") == 8


def test_float_numbers():
    assert evaluate("3.5 * 2") == 7


def test_unary_sign():
    assert evaluate("-5") == -5
    assert evaluate("+5") == 5
    assert evaluate("2 * -3") == -6


def test_spaces():
    assert evaluate("  1+1  ") == 2


def test_empty():
    with pytest.raises(ToolkitError):
        evaluate("")


def test_bad_symbol():
    with pytest.raises(ToolkitError):
        evaluate("2 + a")


def test_missing_number():
    with pytest.raises(ToolkitError):
        evaluate("2 +")


def test_two_operators():
    with pytest.raises(ToolkitError):
        evaluate("2 * / 3")


def test_division_by_zero():
    with pytest.raises(ToolkitError):
        evaluate("5 / 0")
