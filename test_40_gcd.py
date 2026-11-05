import importlib
module = importlib.import_module("40_gcd")


def test_gcd_basic():
    assert module.gcd(48, 18) == 6


def test_gcd_coprime():
    assert module.gcd(17, 13) == 1


def test_gcd_with_zero():
    assert module.gcd(0, 5) == 5
