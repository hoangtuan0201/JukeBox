import tkinter as tk
import tkinter.scrolledtext as tkst
import font_manager as fonts
import track_library as lib
from tkinter import messagebox


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Clear any existing text
    text_area.insert(tk.END, content)

class UpdateTrackWindow:
    def __init__(self, window):
        window.geometry("600x500")  # Size of the window
        window.title("Update Track Rating")
        window.configure(bg="#D4BDAC")

        # Title Label
        tk.Label(window, text="Update Track Rating", font=("Helvetica", 16, "bold"), bg="#D4BDAC").grid(row=0, column=0, columnspan=3, pady=10)

        # Label and Entry for Track Number
        tk.Label(window, text="Enter Track Number:", bg="#D4BDAC").grid(row=1, column=0, padx=5, pady=5, sticky="E")
        self.track_number_entry = tk.Entry(window, width=15)
        self.track_number_entry.grid(row=1, column=1, padx=5, pady=5, sticky="W")

        # Label and Entry for New Rating
        tk.Label(window, text="Enter New Rating (1-5):", bg="#D4BDAC").grid(row=2, column=0, padx=5, pady=5, sticky="E")
        self.rating_entry = tk.Entry(window, width=5)
        self.rating_entry.grid(row=2, column=1, padx=5, pady=5, sticky="W")

        # Update Button
        self.update_button = tk.Button(window, text="Update Rating", command=self.update_rating)
        self.update_button.grid(row=3, column=0, columnspan=2, pady=15)

        # ScrolledText widget to display playlist or updates (if needed)
        self.playlist_display = tkst.ScrolledText(window, width=70, height=15, wrap="word")
        self.playlist_display.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        # Status Label
        self.status_label = tk.Label(window, text="", font=("Helvetica", 10), bg="#D4BDAC")
        self.status_label.grid(row=5, column=0, columnspan=3, pady=5)

    def update_rating(self):
        key = self.track_number_entry.get().strip()  # Get track number from entry
        rating_input = self.rating_entry.get().strip()

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
            track = lib.library[key]
            lib.set_rating(key, new_rating)  # Corrected to pass the parsed integer
            content = f"{track.name} - {track.artist} Play Count: {track.play_count}  Rating: {track.stars()}\n"
            set_text(self.playlist_display, content)  # Assuming this displays track info correctly
            messagebox.showinfo("Success", "Track rating updated successfully!")
        else:
            messagebox.showerror("Error", f"Track number {key} is invalid.")


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    UpdateTrackWindow(window)
    window.mainloop()