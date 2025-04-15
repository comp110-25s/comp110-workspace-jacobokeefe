"""Unit tests for dictionary functions"""

__author__ = "730574207"

import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


# Tests for Invert


def test_invert_duplicate() -> None:
    """Edge case: test for KeyError with duplicate keys"""


with pytest.raises(KeyError):
    invert({"kris": "jordan", "michael": "jordan"})


def test_invert_pair() -> None:
    """Use case: test if invert works with single pair"""
    input_dict = {"apple": "cat"}
    expected = {"cat": "apple"}
    assert invert(input_dict) == expected


def test_invert_normal() -> None:
    """Use case: test if invert correctly swaps in normal dictionary"""
    input_dict = {"a": "z", "b": "y", "c": "x"}
    expected = {"z": "a", "y": "b", "x": "c"}
    assert invert(input_dict) == expected


# Tests for Count


def test_count_empty_list() -> None:
    """Edge case: test if an empty dictionary is returned for an empty list"""
    assert count([]) == {}


def test_count_duplicated_items() -> None:
    """Use case: test if count works for list with duplicates"""
    input_list = ["steak", "steak", "steak"]
    expected = {"steak": 3}
    assert count(input_list) == expected


def test_count_unique_items() -> None:
    """Use case: test if count works for list with unique items"""
    input_list = ["shark", "snake", "crocodile"]
    expected = {"shark": 1, "snake": 1, "crocodile": 1}
    assert count(input_list) == expected


# Tests for Favorite Color


def test_favorite_color_empty() -> None:
    """Edge case: test for empty string for empty dictionary"""
    input_dict: dict[str, str] = {}
    expected: str = ""
    assert favorite_color(input_dict) == expected


def test_favorite_color_duplicates() -> None:
    """Use case: test if all colors are the same that it will be the favorite color"""
    input_dict = {"Ron": "red", "Ben": "red", "Sam": "red"}
    expected = "red"
    assert favorite_color(input_dict) == expected


def test_favorite_color_normal() -> None:
    """Use case: test if it outputs correct favorite color from normal list"""
    input_dict = {"Ron": "red", "Stacy": "red", "Jerry": "blue"}
    expected = "red"
    assert favorite_color(input_dict) == expected


# Tests for bin_len


def test_bin_len_empty_list() -> None:
    """Edge case: test if an empty dictionary is returned for an empty list"""
    assert bin_len([]) == {}


def test_bin_len_duplicated_items() -> None:
    """Use case: tests if bin_len handles duplicate words once"""
    input_list = ["steak", "steak", "shark"]
    expected = {5: {"steak", "shark"}}
    assert bin_len(input_list) == expected


def test_bin_len_unique_items() -> None:
    """Use case: tests to see if bin_len function works with normal list of words. Specifically, if it correctly associates word lengths with words."""
    input_list = ["shark", "snake", "crocodile"]
    expected = {5: {"shark", "snake"}, 9: {"crocodile"}}
    assert bin_len(input_list) == expected
