import pytest
from model.library_item import LibraryItem, LibraryItemPodcast, LibraryItemAlbum


# Test the basic LibraryItem class
def test_library_item_initialization():
    item = LibraryItem("Imagine", "John Lennon", "imagine.jpg", "https://youtu.be/YkgkThdzX-8", 5)

    assert item.name == "Imagine"
    assert item.artist == "John Lennon"
    assert item.picture == "imagine.jpg"
    assert item.youtube_link == "https://youtu.be/YkgkThdzX-8"
    assert item.rating == 5
    assert item.play_count == 0


def test_invalid_rating():
    with pytest.raises(ValueError, match="Rating must be an integer between 0 and 5."):
        LibraryItem("Test", "Artist", "test.jpg", "https://youtube.com", 6)


def test_stars():
    item = LibraryItem("Imagine", "John Lennon", "imagine.jpg", "https://youtu.be/YkgkThdzX-8", 3)
    assert item.stars() == "***"


def test_info():
    item = LibraryItem("Imagine", "John Lennon", "imagine.jpg", "https://youtu.be/YkgkThdzX-8", 5)
    expected_info = (
        "Imagine - John Lennon\n"
        "Rating: ***** | Plays: 0\n"
        "Watch: https://youtu.be/YkgkThdzX-8\n"
    )
    assert item.info() == expected_info


# Test the LibraryItemPodcast subclass
def test_podcast_initialization():
    podcast = LibraryItemPodcast("AI and the Future", "TechTalk", "podcast.jpg", "https://youtu.be/TechPodcast", 75, 12,
                                 "TechTalk Weekly", 4)

    assert podcast.name == "AI and the Future"
    assert podcast.artist == "TechTalk"
    assert podcast.duration == 75
    assert podcast.episode_number == 12
    assert podcast.series_name == "TechTalk Weekly"
    assert podcast.rating == 4


def test_podcast_info():
    podcast = LibraryItemPodcast("AI and the Future", "TechTalk", "podcast.jpg", "https://youtu.be/TechPodcast", 75, 12,
                                 "TechTalk Weekly", 4)
    expected_info = (
        "Podcast Series: TechTalk Weekly - Episode 12\n"
        "AI and the Future by TechTalk\n"
        "Duration: 75 minutes | Rating: **** | Plays: 0\n"
        "Watch: https://youtu.be/TechPodcast"
    )
    assert podcast.podcast_info() == expected_info


def test_is_long_episode():
    podcast = LibraryItemPodcast("AI and the Future", "TechTalk", "podcast.jpg", "https://youtu.be/TechPodcast", 75, 12,
                                 "TechTalk Weekly", 4)
    assert podcast.is_long_episode() == True


# Test the LibraryItemAlbum subclass
def test_album_initialization():
    album = LibraryItemAlbum("Bohemian Rhapsody", "Queen", "queen_album.jpg", "https://youtu.be/fJ9rUzIMcZQ",
                             "A Night at the Opera", 1975, 5)

    assert album.name == "Bohemian Rhapsody"
    assert album.artist == "Queen"
    assert album.album_name == "A Night at the Opera"
    assert album.release_year == 1975
    assert album.rating == 5


def test_album_info():
    album = LibraryItemAlbum("Bohemian Rhapsody", "Queen", "queen_album.jpg", "https://youtu.be/fJ9rUzIMcZQ",
                             "A Night at the Opera", 1975, 5)
    expected_info = (
        "Album: A Night at the Opera (1975)\n"
        "Track: Bohemian Rhapsody by Queen\n"
        "Rating: ***** | Plays: 0\n"
        "Watch: https://youtu.be/fJ9rUzIMcZQ"
    )
    assert album.album_info() == expected_info


def test_is_classic():
    album = LibraryItemAlbum("Bohemian Rhapsody", "Queen", "queen_album.jpg", "https://youtu.be/fJ9rUzIMcZQ",
                             "A Night at the Opera", 1975, 5)
    assert album.is_classic() == True

