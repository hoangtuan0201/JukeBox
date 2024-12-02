import pytest
from model.library_item import LibraryItem

def test_library_item_initialization():

    item = LibraryItem("DEMO1", "DEMO1", 3)
    assert item.name == "DEMO1"
    assert item.artist == "DEMO1"
    assert item.rating == 3
    assert item.play_count == 0

def test_library_item_invalid_rating():
    with pytest.raises(ValueError):
        LibraryItem("Demo", "Demo", 6)  # Invalid rating

def test_info_method():
    item = LibraryItem("va the la het", "Chillies ", 4)
    assert item.info() == "va the la het - Chillies  ****"

def test_stars_method():
    item = LibraryItem("va the la het", "Chillies", 2)
    assert item.stars() == "**"

