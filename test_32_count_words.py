import importlib
module = importlib.import_module("32_count_words")


def test_count_normal():
    assert module.count_words("I love Python programming") == 4


def test_count_extra_spaces():
    assert module.count_words("  hello    world  ") == 2


def test_count_empty():
    assert module.count_words("") == 0
