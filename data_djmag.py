import requests
from bs4 import BeautifulSoup
import csv

class Track:
    """Represents a single music track."""
    def __init__(self, artist: str, title: str, label: str):
        self.artist = artist
        self.title = title
        self.label = label

    def __repr__(self):
        return f"{self.artist} - {self.title} [{self.label}]"


class DJMagScraper:
    """Scraper for DJ Mag Top Tracks page."""
    def __init__(self, url: str):
        self.url = url
        self.tracks = []

    def fetch_page(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")

    def parse_tracks(self):
        soup = self.fetch_page()
        artists = soup.find_all("div", class_="field--name-field-list-number")
        titles = soup.find_all("div", class_="field--name-field-list-title")

        for artist, title in zip(artists, titles):
            artist_name = artist.get_text(strip=True)
            track_info = title.get_text(strip=True)

            # Split into title and label
            if "[" in track_info and "]" in track_info:
                track_title = track_info.split("[")[0].strip().strip("'")
                label = track_info.split("[")[-1].replace("]", "").strip()
            else:
                track_title, label = track_info, ""

            self.tracks.append(Track(artist_name, track_title, label))

        return self.tracks


class TrackExporter:
    """Exports tracks to CSV or TXT."""
    @staticmethod
    def to_csv(tracks, filename="djmag_tracks.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Artist", "Track", "Label"])
            for track in tracks:
                writer.writerow([track.artist, track.title, track.label])

    @staticmethod
    def to_txt(tracks, filename="djmag_tracks.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            for track in tracks:
                f.write(f"{track}\n")


# Example usage
if __name__ == "__main__":
    url = "https://djmag.com/features/dj-mag-top-tracks-2023"
    scraper = DJMagScraper(url)
    tracks = scraper.parse_tracks()

    # Show first few
    for t in tracks[:5]:import requests
from bs4 import BeautifulSoup
import csv

class Track:
    """Represents a single music track."""
    def __init__(self, artist: str, title: str, label: str):
        self.artist = artist
        self.title = title
        self.label = label

    def __repr__(self):
        return f"{self.artist} - {self.title} [{self.label}]"


class DJMagScraper:
    """Scraper for DJ Mag Top Tracks page."""
    def __init__(self, url: str):
        self.url = url
        self.tracks = []

    def fetch_page(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")

    def parse_tracks(self):
        soup = self.fetch_page()
        artists = soup.find_all("div", class_="field--name-field-list-number")
        titles = soup.find_all("div", class_="field--name-field-list-title")

        for artist, title in zip(artists, titles):
            artist_name = artist.get_text(strip=True)
            track_info = title.get_text(strip=True)

            # Split into title and label
            if "[" in track_info and "]" in track_info:
                track_title = track_info.split("[")[0].strip().strip("'")
                label = track_info.split("[")[-1].replace("]", "").strip()
            else:
                track_title, label = track_info, ""

            self.tracks.append(Track(artist_name, track_title, label))

        return self.tracks


class TrackExporter:
    """Exports tracks to CSV or TXT."""
    @staticmethod
    def to_csv(tracks, filename="djmag_tracks.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Artist", "Track", "Label"])
            for track in tracks:
                writer.writerow([track.artist, track.title, track.label])

    @staticmethod
    def to_txt(tracks, filename="djmag_tracks.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            for track in tracks:
                f.write(f"{track}\n")


# Example usage
if __name__ == "__main__":
    url = "https://djmag.com/features/dj-mag-top-tracks-2023"
    scraper = DJMagScraper(url)
    tracks = scraper.parse_tracks()

    # Show first few
    for t in tracks[:5]:
        print(t)

    # Export
    TrackExporter.to_csv(tracks)
    TrackExporter.to_txt(tracks)

        print(t)

    # Export
    TrackExporter.to_csv(tracks)
    TrackExporter.to_txt(tracks)


