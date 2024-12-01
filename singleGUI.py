import tkinter as tk
from tkinter import ttk
import font_manager as fonts
import tkinter.scrolledtext as tkst
from create_track_list import Playlist
import track_library as lib
from tkinter import messagebox


album1 = Playlist("album1")
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Clear any existing text
    text_area.insert(tk.END, content)
class JukeboxApp:

############################ UI COMPONENTS ##########
    def __init__(self, root):
        root.title("Jukebox")
        root.geometry("1366x800")
        root.configure(bg="#FFF1DB")  # Background color

        # Header Section
        header_frame = tk.Frame(root, bg="#88C273", height=10)
        header_frame.pack(fill="x", side="top")

        title_label = tk.Label(header_frame, text="Jukebox Application", fg="black", bg="#88C273")
        title_label.pack()

        # Search and Filter Section
        search_frame = tk.LabelFrame(root, text="Search and Filter", bg="#FFF1DB", fg="black")
        search_frame.pack(fill="x", padx=10, pady=10)



        tk.Label(search_frame, text="Search (Track/Artist):", bg="#FFF1DB", fg="black").grid(row=0, column=1, padx=5, pady=5)
        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.grid(row=0, column=2, padx=5, pady=5)

        search_btn = tk.Button(search_frame, text="Search", bg="#88C273", fg="black", command=self.search_tracks)
        search_btn.grid(row=0, column=3, padx=5, pady=5)

        clear_btn = tk.Button(search_frame, text="Clear", bg="#D4BDAC", fg="black", command=lambda: self.available_list.delete("1.0", tk.END))
        clear_btn.grid(row=0, column=4, padx=5, pady=5)

        filter_label = tk.Label(search_frame, text="Filter by:", bg="#FFF1DB", fg="black")
        filter_label.grid(row=0, column=5, padx=5, pady=5)


        self.filter_option = ttk.Combobox(search_frame, values=["No Filter", "Rating", "Play Count"])
        self.filter_option.grid(row=0, column=6, padx=5, pady=5)
        # Set the default value for the Combobox
        self.filter_option.set("No Filter")

        filter_btn = tk.Button(search_frame, text="Apply Filter", bg="#88C273", fg="black", command=self.filter_tracks)
        filter_btn.grid(row=0, column=7, padx=5, pady=5)

############################Tracks List Section#############
        lists_frame = tk.Frame(root, bg="#FFF1DB")
        lists_frame.pack(fill="both", expand=True, padx=10, pady=10)

        available_frame = tk.LabelFrame(lists_frame, text="Tracks Available", bg="#FFF1DB", fg="black")
        available_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.available_list = tkst.ScrolledText(available_frame, height=10, width=50, bg="white", fg="black")
        self.available_list.pack(fill="both", expand=True, padx=10, pady=10)
        # Add button to list all tracks
        list_all_tracks_btn = tk.Button(available_frame, text="List All Tracks", bg="#88C273", fg="black",command=self.display_available_tracks)
        list_all_tracks_btn.pack(side="left", pady=10,padx=10)

###############################My Playlist Section #############################
        my_list_frame = tk.LabelFrame(lists_frame, text="My Playlist", bg="#FFF1DB", fg="black")
        my_list_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.playlist_display = tkst.ScrolledText(my_list_frame, height=8, width=40, bg="white", fg="black")
        self.playlist_display.pack(fill="both", expand=True, padx=10, pady=10)

        add_track_frame = tk.Frame(my_list_frame, bg="#FFF1DB")
        add_track_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(add_track_frame, text="Enter Track Number:", bg="#FFF1DB", fg="black").pack(side="left", padx=5)

        self.track_number_entry = tk.Entry(add_track_frame, width=10)
        self.track_number_entry.pack(side="left", padx=5)

        add_track_btn = tk.Button(add_track_frame, text="Add To Playlist", bg="#88C273", fg="black", command=self.add_to_playlist)
        add_track_btn.pack(side="left", padx=5)
        play_playlist_btn = tk.Button(add_track_frame, text="Play Playlist", bg="#88C273", fg="black", command=self.play_playlist)
        play_playlist_btn.pack(side="left", padx=5)
        reset_track_btn = tk.Button(add_track_frame, text="Reset Playlist", bg="#D4BDAC", fg="black", command=self.reset_playlist)
        reset_track_btn.pack(side="left", padx=5)



###################### Update Rating and ViewTrack ###########################################
        info_frame = tk.LabelFrame(root, text="View Track and Update Rating", bg="#FFF1DB", fg="black")
        info_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(info_frame, text="Track ID:", bg="#FFF1DB", fg="black").grid(row=0, column=0, padx=5, pady=5)
        self.track_id_entry = tk.Entry(info_frame, width=10)
        self.track_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(info_frame, text="New Rating:", bg="#FFF1DB", fg="black").grid(row=0, column=2, padx=5, pady=5)
        self.new_rating_entry = tk.Entry(info_frame, width=10)
        self.new_rating_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Button(info_frame, text="View Track", bg="#88C273", fg="black", command=self.view_track).grid(row=0, column=4, padx=5, pady=5)
        tk.Button(info_frame, text="Update", bg="#88C273", fg="black", command=self.update_rating).grid(row=0, column=5, padx=5, pady=5)
        self.track_details = tk.Text(info_frame, height=10, width=50, bg="white", fg="black")
        self.track_details.grid(row=1, column=0, columnspan=5, padx=5)

        # Label for track image
        self.image_label = tk.Label(info_frame, bg="#FFF1DB")
        self.image_label.grid(row=1, column=6, padx=5)

############################## FUNCTIONS #########################
    #SEARCH AND SORT FUNCTIONS
    def search_tracks(self):
        query = self.search_entry.get().lower()

        if not query:
            set_text(self.available_list, "Please fill in the search field")
            return

        results = []
        for key, track in lib.library.items():
            if query in track.name.lower() or query in track.artist.lower():
                results.append(f"{key} {track.name} - {track.artist} - {track.stars()} url:{track.youtube_link} plays:{track.play_count}" )

        if results:
            set_text(self.available_list, "\n".join(results))
        else:
            set_text(self.available_list, f"No results found for '{query}'")

    def filter_tracks(self):
        criteria = self.filter_option.get()
        tracks = list(lib.library.values())
        if criteria == "No Filter":
            self.display_available_tracks()
            return


        if criteria == "Rating":
            # Sort by rating in descending order
            sorted_tracks = sorted(tracks, key=lambda t: t.rating, reverse=True)
        elif criteria == "Play Count":
            # Sort by play count in descending order
            sorted_tracks = sorted(tracks, key=lambda t: t.play_count, reverse=True)
        else:
            set_text(self.available_list, "Invalid filter criteria selected.")
            return

        # Format and display the sorted tracks
        results = [t.info() for t in sorted_tracks]
        set_text(self.available_list, "\n".join(results))

    #VIEW TRACK FUNCTIONS
    def display_available_tracks(self):
        """Display the available tracks in the Available Tracks text area."""
        track_list = lib.list_all()
        set_text(self.available_list, track_list)
        
    #PLAYLIST FUNCTIONS#
    def add_to_playlist(self):
        """Add a track to the playlist based on track number."""
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

    def display_playlist(self):
        """Display the playlist in My Playlist text area."""
        if not album1.songs:
            set_text(self.playlist_display, "Playlist is empty.\n")
        else:
            content = "Current Playlist:\n"
            for track in album1.songs:
                content += f"{track.name} - {track.artist} (Play Count: {track.play_count})\n"
            set_text(self.playlist_display, content)

    def play_playlist(self):
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

    def reset_playlist(self):
        """Reset the playlist and clear the text area."""
        album1.songs = []  # Clear the playlist
        self.display_playlist()
        messagebox.showinfo("Info", "Playlist has been reset.")

    #UPDATE RATING FUNCTIONS#

    def view_track(self):
        key = self.track_id_entry.get()  # Gets the track number from the input
        if key in lib.library:
            track = lib.library[key]
            content = (f"{track.name}\n{track.artist}\nrating: {track.rating}\nplays: {track.play_count}\nURL:{track.youtube_link}")
            set_text(self.track_details, content)  # Displays track details in the text widget
            #display image for each track
            try:
                self.track_img = tk.PhotoImage(file=track.picture)
                self.image_label.configure(image=self.track_img)

            except Exception as e:
                set_text(self.track_details, f"Error loading image: {e}")
        else:
            set_text(self.track_details, f"Track {key} not found")  # Displays a not found message
            self.image_label.configure(image="")  # Clears the image label when track is not found

    def update_rating(self):
        key = self.track_id_entry.get().strip()  # Get track number from entry
        rating_input = self.new_rating_entry.get().strip()

        # Check if any fields are empty
        if not key or not rating_input:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Validate that the key is a number
        if not key.isdigit():
            messagebox.showerror("Error", "Track number must be a numeric value.")
            return

        # Validate and parse the rating
        try:
            new_rating = int(rating_input)
            if new_rating < 1 or new_rating > 5:
                messagebox.showerror("Error", "Rating must be between 1 and 5.")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric rating.")
            return

        # Check if the track number exists in the library
        if key in lib.library:

            lib.set_rating(key, new_rating)  # Corrected to pass the parsed integer
            self.view_track()
            messagebox.showinfo("Success", "Track rating updated successfully!")
        else:
            messagebox.showerror("Error", f"Track number {key} is invalid.")


if __name__ == "__main__":
    root = tk.Tk()
    app = JukeboxApp(root)
    fonts.configure()
    root.mainloop()
