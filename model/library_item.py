class LibraryItem:
    def __init__(self, name, artist, picture, youtube_link, rating=0):
        self.name = name
        self.artist = artist
        if isinstance(rating, int) and 0 <= rating <= 5:
            self.rating = rating
        else:
            raise ValueError("Rating must be an integer between 0 and 5.")
        self.youtube_link = youtube_link  # YouTube video link for the track or podcast episode
        self.picture = picture  # File path for an image
        self.play_count = 0

    def info(self):
        """Provides basic information about the library item."""
        return (
            f"{self.name} - {self.artist}\n"
            f"Rating: {self.stars()} | Plays: {self.play_count}\n"
            f"Watch: {self.youtube_link}\n"
        )

    def stars(self):
        """Returns a star rating string."""
        return "*" * self.rating



class LibraryItemPodcast(LibraryItem):
    def __init__(self, name, artist, picture, youtube_link, duration, episode_number, series_name, rating=0):
        super().__init__(name, artist, picture, youtube_link, rating)
        self.duration = duration  # Duration in minutes
        self.episode_number = episode_number
        self.series_name = series_name

    def podcast_info(self):
        """Provides detailed podcast-specific information."""
        return (
            f"Podcast Series: {self.series_name} - Episode {self.episode_number}\n"
            f"{self.name} by {self.artist}\n"
            f"Duration: {self.duration} minutes | Rating: {self.stars()} | Plays: {self.play_count}\n"
            f"Watch: {self.youtube_link}"
        )

    def is_long_episode(self):
        """Determine if the podcast episode is longer than 60 minutes."""
        return self.duration > 60


class LibraryItemAlbum(LibraryItem):
    def __init__(self, name, artist, picture, youtube_link, album_name, release_year, rating=0):
        super().__init__(name, artist, picture, youtube_link, rating)
        self.album_name = album_name
        self.release_year = release_year

    def album_info(self):
        """Provides detailed album-specific information."""
        return (
            f"Album: {self.album_name} ({self.release_year})\n"
            f"Track: {self.name} by {self.artist}\n"
            f"Rating: {self.stars()} | Plays: {self.play_count}\n"
            f"Watch: {self.youtube_link}"
        )

    def is_classic(self):
        """Determine if the album is a classic (older than 25 years)."""
        import datetime
        current_year = datetime.datetime.now().year
        return current_year - self.release_year > 25

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song, track_number):
        song.track_number = track_number
        self.songs.append(song)

# Example Usage
# if __name__ == "__main__":
#     # Creating a basic library item
#     track = LibraryItem(
#         name="Imagine",
#         artist="John Lennon",
#         picture="imagine.jpg",
#         youtube_link="https://youtu.be/YkgkThdzX-8",
#         rating=5
#     )
#     print(track.info())
#
#     # Creating a podcast episode
#     podcast = LibraryItemPodcast(
#         name="AI and the Future",
#         artist="TechTalk",
#         picture="podcast.jpg",
#         youtube_link="https://youtu.be/TechPodcast",
#         duration=75,
#         episode_number=12,
#         series_name="TechTalk Weekly",
#         rating=4
#     )
#     print(podcast.podcast_info())
#     print("Is long episode:", podcast.is_long_episode())
#
#     # Creating an album track
#     album_track = LibraryItemAlbum(
#         name="Bohemian Rhapsody",
#         artist="Queen",
#         picture="queen_album.jpg",
#         youtube_link="https://youtu.be/fJ9rUzIMcZQ",
#         album_name="A Night at the Opera",
#         release_year=1975,
#         rating=5
#     )
#     print(album_track.album_info())
#     print("Is classic album:", album_track.is_classic())
