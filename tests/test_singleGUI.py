import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
from singleGUI import JukeboxApp
import track_library as lib  # Assuming lib is where library data and methods are defined


class TestJukeboxApp(unittest.TestCase):

    def setUp(self):
        """Set up the root window and the JukeboxApp."""
        self.root = tk.Tk()
        self.app = JukeboxApp(self.root)
        self.app.search_entry = MagicMock()
        self.app.track_number_entry = MagicMock()
        self.app.track_id_entry = MagicMock()
        self.app.new_rating_entry = MagicMock()

    def tearDown(self):
        """Clean up after each test."""
        self.root.quit()

    def test_search_tracks(self):
        """Test search functionality."""
        # Simulate search input
        self.app.search_entry.get.return_value = "Artist Name"

        # Mock the lib.library with a sample track
        mock_track = MagicMock()
        mock_track.name = "Song Name"
        mock_track.artist = "Artist Name"
        mock_track.stars.return_value = "⭐⭐⭐⭐⭐"
        mock_track.youtube_link = "https://youtube.com"
        mock_track.play_count = 10
        lib.library = {1: mock_track}



    def test_add_to_playlist(self):
        """Test adding a track to the playlist."""
        # Mock track number entry and lib.library
        self.app.track_number_entry.get.return_value = "1"
        mock_track = MagicMock()
        mock_track.track_number = 1
        lib.library = {1: mock_track}

        with patch.object(self.app, 'display_playlist') as mock_display_playlist:
            self.app.add_to_playlist()
            mock_display_playlist.assert_called_once()  # Ensure playlist is updated after adding

    def test_add_to_playlist_invalid_track(self):
        """Test adding an invalid track to the playlist."""
        self.app.track_number_entry.get.return_value = "999"  # Invalid track number

        with patch('tkinter.messagebox.showerror') as mock_showerror:
            self.app.add_to_playlist()
            mock_showerror.assert_called_once_with("Error", "Track number 999 is invalid.")  # Check error message

    def test_update_rating(self):
        """Test updating a track rating."""
        # Mock track ID entry and rating entry
        self.app.track_id_entry.get.return_value = "1"
        self.app.new_rating_entry.get.return_value = "4"

        # Mock lib.library and set_rating method
        mock_track = MagicMock()
        lib.library = {"1": mock_track}

        with patch('tkinter.messagebox.showinfo') as mock_showinfo:
            self.app.update_rating()
            mock_track.set_rating.assert_called_once_with("1", 4)  # Ensure rating was updated
            mock_showinfo.assert_called_once_with("Success", "Track rating updated successfully!")

    def test_invalid_rating(self):
        """Test invalid rating input."""
        self.app.track_id_entry.get.return_value = "1"
        self.app.new_rating_entry.get.return_value = "invalid"

        with patch('tkinter.messagebox.showerror') as mock_showerror:
            self.app.update_rating()
            mock_showerror.assert_called_once_with("Error", "Please enter a valid numeric rating.")

    def test_display_available_tracks(self):
        """Test displaying all tracks."""
        mock_track = MagicMock()
        mock_track.info.return_value = "Track 1 info"
        lib.list_all = MagicMock(return_value="Track 1 info")

        with patch.object(self.app.available_list, 'insert') as mock_insert:
            self.app.display_available_tracks()
            mock_insert.assert_called_once_with(tk.END, "Track 1 info")

    def test_reset_playlist(self):
        """Test resetting the playlist."""
        self.app.reset_playlist()
        self.app.playlist_display.insert.assert_called_once_with(tk.END,
                                                                 "Playlist is empty.\n")  # Check if reset message is shown


if __name__ == "__main__":
    unittest.main()
