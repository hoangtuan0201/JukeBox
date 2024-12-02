import csv
from model.library_item import LibraryItem

# Path to the CSV file storing library data
CSV_FILE_PATH = "track_library.csv"

library = {}



def load_library_from_csv():
    """Load track library from a CSV file."""
    global library
    library = {}
    try:
        with open(CSV_FILE_PATH, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                library[row["TrackID"]] = LibraryItem(
                    name=row["Name"],
                    artist=row["Artist"],
                    picture=row["Picture"],
                    youtube_link=row["YouTubeLink"],
                    rating=int(row["Rating"]),
                )
                library[row["TrackID"]].play_count = int(row["PlayCount"])
    except FileNotFoundError:
        print(f"File '{CSV_FILE_PATH}' not found. Starting with an empty library.")
    except Exception as e:
        print(f"Error loading library: {e}")


def save_library_to_csv():
    """Save the current library to a CSV file."""
    try:
        with open(CSV_FILE_PATH, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["TrackID", "Name", "Artist", "Picture", "YouTubeLink", "Rating", "PlayCount"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for track_id, item in library.items():
                writer.writerow({
                    "TrackID": track_id,
                    "Name": item.name,
                    "Artist": item.artist,
                    "Picture": item.picture,
                    "YouTubeLink": item.youtube_link,
                    "Rating": item.rating,
                    "PlayCount": item.play_count,
                })

    except Exception as e:
        print(f"Error saving library: {e}")


# Automatically load the library on import
load_library_from_csv()

def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
        save_library_to_csv()  # Save changes
    except KeyError:
        return


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
        save_library_to_csv()  # Save changes
    except KeyError:
        return
#Old function
def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output

def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1

def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1

def get_artist(key):
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None

def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None

print(list_all())