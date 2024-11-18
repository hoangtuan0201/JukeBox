import tkinter as tk


import font_manager as fonts
from view_tracks import TrackViewer


def view_tracks_clicked():
    status_lbl.configure(text="View Tracks button was clicked!")
    TrackViewer(tk.Toplevel(window))


window = tk.Tk()
window.geometry("520x150")
window.title("JukeBox")
window.configure(bg="gray")

fonts.configure()

header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

view_tracks_btn = tk.Button(window, text="View Tracks", command=view_tracks_clicked)
view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

create_track_list_btn = tk.Button(window, text="Create Track List")
create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)

update_tracks_btn = tk.Button(window, text="Update Tracks")
update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

status_lbl = tk.Label(window, bg='gray', text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
