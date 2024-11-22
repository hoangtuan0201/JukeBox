from library_item import LibraryItem


library = {
    "01": LibraryItem("Another Brick in the Wall", "Pink Floyd", "pictures/pinkfloyd.png", 4),
    "02": LibraryItem("Stayin' Alive", "Bee Gees", "pictures/beegees.png", 5),
    "03": LibraryItem("Highway to Hell", "AC/DC", "pictures/acdc.png", 2),
    "04": LibraryItem("Shape of You", "Ed Sheeran", "pictures/edsheeran.png", 1),
    "05": LibraryItem("Someone Like You", "Adele", "pictures/adele.png", 3),
    "06": LibraryItem("Am Tham Ben Em", "Son Tung MTP", "pictures/sontung.png", 5),
}



def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_artist(key):
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return

def set_picture(key, picture):
    try:
        item = library[key]
        item.picture = picture
    except KeyError:
        return