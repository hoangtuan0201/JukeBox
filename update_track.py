import tkinter as tk
import tkinter.scrolledtext as tkst
import font_manager as fonts
import track_library as lib

class UpdateTrackWindow:
    def __init__(self, window):
        window.geometry("600x500")
        window.title("Update Track Details")
        window.configure(bg="#D4BDAC")  # Set background color

        # Title Label
        tk.Label(window, text="Update Track Information", font=("Helvetica", 16, "bold"), bg="#D4BDAC").grid(row=0,
                                                                                                             column=0,
                                                                                                             columnspan=2,
                                                                                                             pady=10)

        # Label and entry for track ID
        tk.Label(window, text="Track ID:", bg="#D4BDAC").grid(row=1, column=0, padx=10, pady=5, sticky="E")
        self.track_id_entry = tk.Entry(window, width=30)
        self.track_id_entry.grid(row=1, column=1, padx=10, pady=5, sticky="W")

        # Label and entry for updating track name
        tk.Label(window, text="New Track Name:", bg="#D4BDAC").grid(row=2, column=0, padx=10, pady=5, sticky="E")
        self.track_name_entry = tk.Entry(window, width=30)
        self.track_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="W")

        # Label and entry for updating artist name
        tk.Label(window, text="New Artist Name:", bg="#D4BDAC").grid(row=3, column=0, padx=10, pady=5, sticky="E")
        self.artist_name_entry = tk.Entry(window, width=30)
        self.artist_name_entry.grid(row=3, column=1, padx=10, pady=5, sticky="W")

        # Label and entry for updating rating
        tk.Label(window, text="New Rating (1-5):", bg="#D4BDAC").grid(row=4, column=0, padx=10, pady=5, sticky="E")
        self.rating_entry = tk.Entry(window, width=5)
        self.rating_entry.grid(row=4, column=1, padx=10, pady=5, sticky="W")

        # Label and entry for updating play count
        tk.Label(window, text="New Play Count:", bg="#D4BDAC").grid(row=5, column=0, padx=10, pady=5, sticky="E")
        self.play_count_entry = tk.Entry(window, width=10)
        self.play_count_entry.grid(row=5, column=1, padx=10, pady=5, sticky="W")

        # Button to submit the updates
        update_btn = tk.Button(window, text="Update Track",)
        update_btn.grid(row=6, column=0, columnspan=2, pady=20)

        # ScrolledText widget to display track update status
        self.status_display = tkst.ScrolledText(window, width=70, height=10, wrap="word")
        self.status_display.grid(row=7, column=0, columnspan=2, padx=10, pady=10)


if __name__ == "__main__":
    # Create the main window
    create_window = tk.Tk()
    fonts.configure()
    UpdateTrackWindow(create_window)
    create_window.mainloop()


