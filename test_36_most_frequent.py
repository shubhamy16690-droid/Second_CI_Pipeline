import importlib
module = importlib.import_module("36_most_frequent")


def test_most_frequent_basic():
    assert module.most_frequent([1, 3, 2, 3, 3, 1]) == 3


def test_most_frequent_single():
    assert module.most_frequent([5]) == 5


def test_most_frequent_empty():
    assert module.most_frequent([]) is None
