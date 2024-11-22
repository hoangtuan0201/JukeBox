class LibraryItem:
    def __init__(self, name, artist, picture, rating=0):
        self.name = name
        self.artist = artist
        if isinstance(rating, int) and 0 <= rating <= 5:
            self.rating = rating
        else:
            raise ValueError("Rating must be an integer between 0 and 5.")
        self.picture = picture  # File path for an image
        self.play_count = 0


    def info(self):
        return f"{self.name} - {self.artist} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars


