import tkinter as tk
import tkinter.scrolledtext as tkst
import font_manager as fonts
import track_library as lib
from tkinter import messagebox


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Clear any existing text
    text_area.insert(tk.END, content)


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song, track_number):
        song.track_number = track_number
        self.songs.append(song)
#create instance for Playlist class
album1 = Playlist("Album1")

class PlaylistApp:
    def __init__(self, window):

        window.geometry("600x500")
        window.title("Playlist Manager")
        window.configure(bg="#D4BDAC")

        # Title Label
        tk.Label(window,text="Playlist Manager",font=("Helvetica", 17, "bold"),bg="#D4BDAC",).grid(row=0, column=0, columnspan=3, pady=10)
            # Label and Entry for track number
        tk.Label(window, text="Enter Track Number:", bg="#D4BDAC").grid(row=1, column=0, padx=5, pady=5, sticky="E")
        self.track_number_entry = tk.Entry(window, width=10)
        self.track_number_entry.grid(row=1, column=1, padx=5, pady=5, sticky="W")

        # Buttons
        button_frame = tk.Frame(window, bg="#D4BDAC")
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)

        tk.Button(button_frame, text="Add to Playlist", command=self.add_to_playlist).pack(side="left", padx=5)
        tk.Button(button_frame, text="Play Playlist", command=self.play).pack(side="left", padx=5)
        tk.Button(button_frame, text="Reset Playlist", command=self.reset).pack(side="left", padx=5)

        # ScrolledText widget to display the playlist
        self.playlist_display = tkst.ScrolledText(window, width=70, height=20, wrap="word")
        self.playlist_display.grid(row=3, column=0, columnspan=3)

    def add_to_playlist(self):

        key = self.track_number_entry.get().strip()

        if not key:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if not key.isdigit():
            messagebox.showerror("Error", "Track number must be a numeric value.")
            return

        if key in lib.library:
            # Add track to playlist
            track = lib.library[key]
            album1.add_song(track, key)
            self.display_playlist()
        else:
            messagebox.showerror("Error", f"Track number {key} is invalid.")

    def play(self):
        """Simulate playing the playlist by incrementing play counts."""

        if not album1.songs:
            messagebox.showerror("Error", "Playlist is empty. Add tracks first.")
            return

        # Increment play counts for each track in the playlist using attribute track number in playlist class
        for song in album1.songs:
            key = song.track_number
            lib.increment_play_count(key)

        # Display updated playlist with new play counts
        self.display_playlist()

        # Show confirmation to the user
        messagebox.showinfo("Info", "Playlist played.")

    def reset(self):
        """Reset the playlist and clear the text area."""
        album1.songs = []  # Clear the playlist
        self.display_playlist()
        messagebox.showinfo("Info", "Playlist has been reset.")

    def display_playlist(self):
        """Display the playlist in the text area."""
        if not album1.songs:
            set_text(self.playlist_display, "Playlist is empty.\n")
        else:
            content = "Current Playlist:\n"
            for track in album1.songs:
                content += f"{track.name} - {track.artist} (Play Count: {track.play_count})\n"
            set_text(self.playlist_display, content)


if __name__ == "__main__":

    create_window = tk.Tk()
    fonts.configure()
    PlaylistApp(create_window)
    create_window.mainloop()