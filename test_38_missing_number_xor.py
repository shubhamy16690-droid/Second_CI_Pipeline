import importlib
module = importlib.import_module("38_missing_number_xor")


def test_missing_middle():
    assert module.find_missing_number([1, 2, 4, 5], 5) == 3


def test_missing_first():
    assert module.find_missing_number([2, 3, 4], 4) == 1


def test_missing_last():
    assert module.find_missing_number([1, 2, 3], 4) == 4
