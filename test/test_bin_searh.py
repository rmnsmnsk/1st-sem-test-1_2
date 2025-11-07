from src.bin_search import bin_search


def test_middle():
    assert bin_search([1, 2, 3, 4, 5], 4) == 3


def test_start():
    assert bin_search([1, 2, 3, 4], 2) == 1


def test_not_in_list():
    assert bin_search([1, 2, 3, 4], 5) == -1

def test_single():
    assert bin_search([6], 6) == 0
    assert bin_search([2], 3) == -1

def empty():
    assert bin_search([], 8) == -1

def first():
    assert bin_search([5, 2, 3, 4], 5) == 0

def last():
    assert bin_search([1, 2, 3, 8], 8) == 3