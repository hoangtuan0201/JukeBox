import tkinter as tk
from tkinter import ttk

class UnifiedGUI:

    def __init__(self, root):
        root.title("Jukebox Application")
        root.geometry("900x600")
        root.configure(bg="#D4BDAC")  # Light blue background

        # Header Section
        header_frame = tk.Frame(root, bg="#5DADE2", height=50)
        header_frame.pack(fill="x", side="top")

        title_label = tk.Label(header_frame, text="Jukebox Application", font=("Helvetica", 16, "bold"), fg="white", bg="#5DADE2")
        title_label.pack(pady=10)

        # Search and Filter Section
        search_frame = tk.LabelFrame(root, text="Search and Filter", bg="#D6EAF8", font=("Helvetica", 10, "bold"))
        search_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(search_frame, text="Search in:", bg="#D6EAF8").grid(row=0, column=0, padx=5, pady=5)
        search_option = ttk.Combobox(search_frame, values=["Both", "Track Name", "Artist"])
        search_option.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(search_frame, text="Search term:", bg="#D6EAF8").grid(row=0, column=2, padx=5, pady=5)
        search_entry = tk.Entry(search_frame, width=30)
        search_entry.grid(row=0, column=3, padx=5, pady=5)

        search_btn = tk.Button(search_frame, text="Search", bg="#5DADE2", fg="white")
        search_btn.grid(row=0, column=4, padx=5, pady=5)

        clear_btn = tk.Button(search_frame, text="Clear", bg="#E74C3C", fg="white")
        clear_btn.grid(row=0, column=5, padx=5, pady=5)

        filter_label = tk.Label(search_frame, text="Filter by:", bg="#D6EAF8")
        filter_label.grid(row=0, column=6, padx=5, pady=5)

        filter_option = ttk.Combobox(search_frame, values=["No Filter", "Rating", "Play Count"])
        filter_option.grid(row=0, column=7, padx=5, pady=5)

        filter_btn = tk.Button(search_frame, text="Apply Filter", bg="#5DADE2", fg="white")
        filter_btn.grid(row=0, column=8, padx=5, pady=5)

        # Tracks List Section
        lists_frame = tk.Frame(root, bg="#D6EAF8")
        lists_frame.pack(fill="both", expand=True, padx=10, pady=10)

        available_frame = tk.LabelFrame(lists_frame, text="Tracks Available", bg="#D6EAF8", font=("Helvetica", 10, "bold"))
        available_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        available_list = tk.Listbox(available_frame, height=20)
        available_list.pack(fill="both", expand=True, padx=10, pady=10)

        my_list_frame = tk.LabelFrame(lists_frame, text="My Track List", bg="#D6EAF8", font=("Helvetica", 10, "bold"))
        my_list_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        my_list = tk.Listbox(my_list_frame, height=20)
        my_list.pack(fill="both", expand=True, padx=10, pady=10)

        # Action Buttons
        action_frame = tk.Frame(root, bg="#D6EAF8")
        action_frame.pack(fill="x", padx=10, pady=10)

        tk.Button(action_frame, text="View Track", bg="#5DADE2", fg="white").pack(side="left", padx=5, pady=5)
        tk.Button(action_frame, text="Update Tracks", bg="#5DADE2", fg="white").pack(side="left", padx=5, pady=5)
        tk.Button(action_frame, text="Play Playlist", bg="#27AE60", fg="white").pack(side="left", padx=5, pady=5)
        tk.Button(action_frame, text="Reset Playlist", bg="#E74C3C", fg="white").pack(side="left", padx=5, pady=5)
        tk.Button(action_frame, text="Remove Track", bg="#E74C3C", fg="white").pack(side="left", padx=5, pady=5)
        tk.Button(action_frame, text="Save Playlist", bg="#5DADE2", fg="white").pack(side="left", padx=5, pady=5)
        tk.Button(action_frame, text="Load Playlist", bg="#5DADE2", fg="white").pack(side="left", padx=5, pady=5)

        # Track Information Section
        info_frame = tk.LabelFrame(root, text="Track Information & Update", bg="#D6EAF8", font=("Helvetica", 10, "bold"))
        info_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(info_frame, text="Track ID:", bg="#D6EAF8").grid(row=0, column=0, padx=5, pady=5)
        track_id_entry = tk.Entry(info_frame, width=10)
        track_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(info_frame, text="New Rating:", bg="#D6EAF8").grid(row=0, column=2, padx=5, pady=5)
        new_rating_entry = tk.Entry(info_frame, width=10)
        new_rating_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Button(info_frame, text="Update", bg="#5DADE2", fg="white").grid(row=0, column=4, padx=5, pady=5)

        track_details = tk.Text(info_frame, height=5, width=80)
        track_details.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = UnifiedGUI(root)
    root.mainloop()
