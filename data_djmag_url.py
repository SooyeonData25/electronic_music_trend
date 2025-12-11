import csv

# list of dj mag top track article urls
urls = [
    "https://djmag.com/features/dj-mags-top-tracks-of-2024",
    "https://djmag.com/features/dj-mag-top-tracks-2023",
    "https://djmag.com/features/dj-mags-top-tracks-2022",
    "https://djmag.com/longreads/dj-mags-top-tracks-2021",
    "https://djmag.com/longreads/2020-year-dance-music",
    "https://djmag.com/longreads/dj-mag-top-50-tracks-2019",
    "https://djmag.com/longreads/dj-mag’s-top-50-tracks-2018",
    "https://djmag.com/content/top-50-tracks-2017",
    "https://djmag.com/features/tunes-2016",
    "https://djmag.com/features/tunes-2015"
]

years = [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015]

# File name
output_file = "djmag_top_tracks_urls.csv"

# save to CSV
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Year", "URL"])  # header

    for y, url in zip(years, urls):
        writer.writerow([y, url])

print(f"CSV saved as {output_file}")
