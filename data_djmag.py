import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

class Track:
    """Represents a single music track."""
    def __init__(self, artist: str, title: str, year: int):
        self.artist = artist
        self.title = title
        self.year = year

    def define_bpm(self, bpm: int):
        self.bpm = bpm

    def define_genre(self, genre: str):
        self.genre = genre

    def __repr__(self):
        return f"{self.artist} - {self.title}"


class DJMagScraper:
    """Scraper for DJ Mag Top Tracks page."""
    def __init__(self, url: str):
        self.url = url
        self.tracks = []

        import re
        match = re.search(r"(20\d{2})", url)
        self.year = int(match.group(1)) if match else 0

    def fetch_page(self):
        response = requests.get(self.url)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")

    def parse_tracks(self):
        soup = self.fetch_page()

        if self.year in [2019, 2021, 2022, 2023, 2024]:
            contents = soup.find_all("div", class_="field--name-field-list-number")
            titles = soup.find_all("div", class_="field--name-field-list-title")

            for content, title in zip(contents, titles):
                content_info = content.get_text(strip=True)
                track_info = title.get_text(strip=True)
                # print("content_info", content_info)
                # print("track_info", track_info)

                if self.year in [2023, 2024]:
                    artist_name = content_info

                    # Split into title and label
                    parts_track_info = track_info.split("[")
                    if len(parts_track_info) > 1:
                        track_title = track_info.split("[")[0].strip().strip("'")
                    else:
                        artist_name, track_title = track_info, ""

                if self.year in [2021, 2022]:
                    parts = content_info.split("'")
                    # Split number info into artist an
                    if len(parts) > 1:
                        artist_name = parts[0].strip()
                        track_title = parts[1].strip()
                    else:
                        artist_name, track_title = content_info, ""
                if self.year in [2019]:
                    parts = track_info.split("'")
                    if len(parts) > 1:
                        artist_name = parts[0].strip()
                        track_title = parts[1].strip()
                    else:
                        artist_name, track_title = track_info, ""


                self.tracks.append(Track(artist_name, track_title, self.year))

        if self.year in [2020]:
            for block in soup.find_all("p"):
                text = block.get_text(strip=True)
                if "Track:" in text:  # adjust filter
                    import re
                    parts = re.split(r"[:\[\]‘’]", text)
                    parts = [p.strip() for p in parts if p.strip()]

                    if len(parts) >= 3:
                        artist_name, track_title, label = parts[1], parts[2], parts[-1]
                        self.tracks.append(Track(artist_name, track_title, self.year))

        return self.tracks


class TrackExporter:
    """Exports tracks to CSV or TXT."""
    @staticmethod
    def to_csv(tracks, filename="djmag_tracks.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["DJmag_top_track_year", "artist", "title"])
            for track in tracks:
                writer.writerow([track.year, track.artist, track.title])

# test for top tracks in 2024
# scraper = DJMagScraper("https://djmag.com/features/dj-mag-top-tracks-2023")
# tracks = scraper.parse_tracks()

# scrape data from djmag article urls
if __name__ == "__main__":
    urls = pd.read_csv("djmag_top_tracks_urls.csv")

    all_tracks = []  # store all tracks from all years

    for url in urls["URL"]:   # CSV column header is "URL"
        scraper = DJMagScraper(url)
        tracks = scraper.parse_tracks()
        all_tracks.extend(tracks)   # append results

    # Show preview
    for t in all_tracks[:5]:
        print(t)

    # Export everything
    TrackExporter.to_csv(all_tracks)



