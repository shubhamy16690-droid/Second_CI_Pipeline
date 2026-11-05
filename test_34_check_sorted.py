import importlib
module = importlib.import_module("34_check_sorted")


def test_sorted_true():
    assert module.is_sorted([1, 2, 3, 4, 5]) is True


def test_sorted_false():
    assert module.is_sorted([3, 1, 2]) is False


def test_sorted_empty_and_single():
    assert module.is_sorted([]) is True
    assert module.is_sorted([7]) is True
