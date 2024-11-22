import tkinter as tk
import tkinter.scrolledtext as tkst
import track_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)#clear any existing text in the widget
    text_area.insert(1.0, content)#Inserts the new content at the beginning of the widget


class TrackViewer:

    def __init__(self, window):
        window.geometry("850x350") # Sets the size of the window
        window.title("View Tracks")  # Sets the window title
        window.configure(bg="#D4BDAC")

        # Button to list all tracks
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10) # Places the button in the grid layout
        # Label for prompting user to enter a track number
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10) # Places the label in the grid layout

        # Entry field for user to input a track number
        self.input_txt = tk.Entry(window, width=3) # Entry field with limited width are 3 characters
        self.input_txt.grid(row=0, column=2, padx=10, pady=10) # Places the entry in the grid layout

        # Button to view a specific track's details
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10) # Places the button in the grid layout

        # Scrollable text widget to display the list of all tracks
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=2, sticky="W", padx=10, pady=10)# Places the widget in the grid layout and the colummn will span to three columns

        # Text widget to display the details of a selected track
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=0) #places the widget in the grid layout and aligns the widget to the North and West (top-left) of the cel

        # Label to display the track image
        self.image_label = tk.Label(window, bg="#D4BDAC")
        self.image_label.grid(row=1, column=3, sticky="S")

        # Button to exit the application
        exit_btn = tk.Button(window, text="Exit", command=window.quit)
        exit_btn.grid(row=2, column=2, padx=10, pady=10) # Places the button in the grid layout

        # Label to display the status of the button
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))

        # Label to display the status of the button
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10) # Places the label in the grid layout

        #Automatically list all tracks when start the application
        self.list_tracks_clicked()



    def view_tracks_clicked(self):
        key = self.input_txt.get() #gets the track number from the input

        if key in lib.library:
            track = lib.library[key]
            track_details = (f"{track.name}\n"
                             f"{track.artist}\n"
                             f"rating: {track.rating}\n"
                             f"plays: {track.play_count}")
            set_text(self.track_txt, track_details)    # Displays track details in the text widget
            try:
                self.track_img = tk.PhotoImage(file=track.picture)
                self.image_label.configure(image=self.track_img)

            except Exception as e:
                set_text(self.track_txt, f"Error loading image: {e}")

        else:
            set_text(self.track_txt, f"Track {key} not found") # Displays a not found message
            self.image_label.configure(image="") # Clears the image label when track is not found
        self.status_lbl.configure(text="View Track button was clicked!") # Updates the status label


    def list_tracks_clicked(self):
        track_list = lib.list_all() # Retrieves all information of all tracks in track_library
        set_text(self.list_txt, track_list) # Displays the track list in the scrolled text widget
        # Updates the status label
        self.status_lbl.configure(text="List Tracks button was clicked!")


if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
