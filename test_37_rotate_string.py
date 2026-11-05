import importlib
module = importlib.import_module("37_rotate_string")


def test_rotate_basic():
    assert module.rotate_string("abcdef", 2) == "cdefab"


def test_rotate_k_larger_than_length():
    assert module.rotate_string("abc", 4) == "bca"


def test_rotate_empty():
    assert module.rotate_string("", 3) == ""
