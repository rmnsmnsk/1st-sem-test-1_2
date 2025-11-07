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

def test_empty():
    assert bin_search([], 8) == -1

def test_first():
    assert bin_search([1, 2, 3, 4], 1) == 0

def test_last():
    assert bin_search([1, 2, 3, 8], 8) == 3

def test_invaild_input():
     assert bin_search(None, 5) == -1
     assert bin_search([1, 2, "с"], 5) == -1

def test_unsorted_array():
    assert bin_search([3, 1, 2], 2) == -1
