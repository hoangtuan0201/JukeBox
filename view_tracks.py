import tkinter as tk
import tkinter.scrolledtext as tkst
import track_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Clear any existing text in the widget
    text_area.insert(1.0, content)  # Insert the new content at the beginning of the widget


class TrackViewer:

    def __init__(self, window):
        window.geometry("850x500")  # Adjusted size to fit the filter option
        window.title("View Tracks")  # Sets the window title
        window.configure(bg="#D4BDAC")

        # Button to list all tracks
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        # Label for prompting user to enter a track number
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Entry field for user to input a track number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Button to view a specific track's details
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        # Scrollable text widget to display the list of all tracks
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=2, sticky="W", padx=10, pady=10)

        # Text widget to display the details of a selected track
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=0)

        # Label to display the track image
        self.image_label = tk.Label(window, bg="#D4BDAC")
        self.image_label.grid(row=1, column=3, sticky="S")

        # Button to exit the application
        exit_btn = tk.Button(window, text="Exit", command=window.quit)
        exit_btn.grid(row=4, column=2, padx=10, pady=10)

        # Label to display the status of the button
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=4, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Automatically list all tracks when starting the application
        self.list_tracks_clicked()

    def view_tracks_clicked(self):
        key = self.input_txt.get()  # Gets the track number from the input

        if key in lib.library:
            track = lib.library[key]
            track_details = (f"{track.name}\n"
                             f"{track.artist}\n"
                             f"rating: {track.rating}\n"
                             f"plays: {track.play_count}")
            set_text(self.track_txt, track_details)  # Displays track details in the text widget
            try:
                self.track_img = tk.PhotoImage(file=track.picture)
                self.image_label.configure(image=self.track_img)

            except Exception as e:
                set_text(self.track_txt, f"Error loading image: {e}")

        else:
            set_text(self.track_txt, f"Track {key} not found")  # Displays a not found message
            self.image_label.configure(image="")  # Clears the image label when track is not found
        self.status_lbl.configure(text="View Track button was clicked!")  # Updates the status label

    def list_tracks_clicked(self):
        track_list = lib.list_all()  # Retrieves all information of all tracks in track_library
        set_text(self.list_txt, track_list)  # Displays the track list in the scrolled text widget
        self.status_lbl.configure(text="List Tracks button was clicked!")  # Updates the status label

    # def search_tracks(self):
    #     query = self.search_txt.get().lower()
    #     results = []
    #     for key, track in lib.library.items():
    #         if query in track.name.lower() or query in track.artist.lower():
    #             results.append(f"{key}. {track.name} - {track.artist} - {track.stars()}")
    #     if results:
    #         set_text(self.list_txt, "\n".join(results))
    #     else:
    #         set_text(self.list_txt, f"No results found for '{query}'")
    #
    #     self.status_lbl.configure(text="Search button was clicked!")  # Updates the status label
    #
    # def filter_tracks(self):
    #     criteria = self.filter_var.get()  # Get the selected filter criteria (Rating or Play Count)
    #     tracks = list(lib.library.values())
    #     if criteria == "No Filter":
    #         self.list_tracks_clicked()
    #         return
    #
    #
    #     if criteria == "Rating":
    #         # Sort by rating in descending order
    #         sorted_tracks = sorted(tracks, key=lambda t: t.rating, reverse=True)
    #     elif criteria == "Play Count":
    #         # Sort by play count in descending order
    #         sorted_tracks = sorted(tracks, key=lambda t: t.play_count, reverse=True)
    #     else:
    #         set_text(self.list_txt, "Invalid filter criteria selected.")
    #         return
    #
    #     # Format and display the sorted tracks
    #     results = [t.info() for t in sorted_tracks]
    #     set_text(self.list_txt, "\n".join(results))
    #     self.status_lbl.configure(text=f"Tracks filtered by {criteria.lower()}!")  # Updates the status label


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    TrackViewer(window)
    window.mainloop()
