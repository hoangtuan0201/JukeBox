import tkinter as tk
import tkinter.scrolledtext as tkst
import font_manager as fonts
import track_library as lib

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)#clear any existing text in the widget

    text_area.insert(tk.END, content)

class CreateTrackListWindow:
    def __init__(self, window):
        window.geometry("600x500")
        window.title("Create Track List")
        window.configure(bg="#D4BDAC")  # Set background color

        # Title Label
        tk.Label(window, text="Create New Track", font=("Helvetica", 16, "bold"), bg="#D4BDAC").grid(row=0, column=0,
                                                                                                     columnspan=2,
                                                                                                     pady=10)

        # Label and entry for track name
        tk.Label(window, text="Track Name:", bg="#D4BDAC").grid(row=1, column=0, padx=10, pady=5, sticky="E")
        self.track_name_entry = tk.Entry(window, width=30)
        self.track_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="W")

        # Label and entry for artist name
        tk.Label(window, text="Artist Name:", bg="#D4BDAC").grid(row=2, column=0, padx=10, pady=5, sticky="E")
        self.artist_name_entry = tk.Entry(window, width=30)
        self.artist_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="W")

        # Label and entry for track rating
        tk.Label(window, text="Rating (1-5):", bg="#D4BDAC").grid(row=3, column=0, padx=10, pady=5, sticky="E")
        self.rating_entry = tk.Entry(window, width=5)
        self.rating_entry.grid(row=3, column=1, padx=10, pady=5, sticky="W")

        # Button to submit the new track
        add_btn = tk.Button(window, text="Add Track", command=self.add_track)
        add_btn.grid(row=4, column=0, columnspan=2, pady=20)

        # ScrolledText widget to display added tracks
        self.track_list_display = tkst.ScrolledText(window, width=70, height=10, wrap="word")
        self.track_list_display.grid(row=5, column=0, columnspan=2, padx=10, pady=10)



        self.display_tracks()

    def add_track(self):
        # Logic for adding a track
        track_name = self.track_name_entry.get().strip()
        artist_name = self.artist_name_entry.get().strip()
        # Validate track name
        if not track_name:
            set_text(self.track_list_display, "Error: Track name cannot be empty.\n")
            return

        # Validate artist name
        if not artist_name:
            set_text(self.track_list_display, "Error: Artist name cannot be empty.\n")
            return

        try:
            rating = int(self.rating_entry.get().strip())
        except ValueError:
            set_text(self.track_list_display, "Error: Rating must be a number.\n")
            return

        if not (1 <= rating <= 5):
            set_text(self.track_list_display, "Error: Rating must be between 1 and 5.\n")
            return

        # If all validations pass, add the track
        new_key = str(len(lib.library) + 1).zfill(2)
        new_track = lib.LibraryItem(track_name, artist_name, rating)
        lib.library[new_key] = new_track

        # Clear entry fields
        self.track_name_entry.delete(0, tk.END)
        self.artist_name_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)

        # Refresh displayed track list and it will update the data we fill in the input
        self.display_tracks()




    def display_tracks(self):
        track_list = lib.list_all()
        set_text(self.track_list_display, track_list)
if __name__ == "__main__":
    # Create the main window
    create_window = tk.Tk()
    fonts.configure()
    CreateTrackListWindow(create_window)
    create_window.mainloop()
