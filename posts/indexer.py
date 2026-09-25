import json
from pathlib import Path
from datetime import datetime

posts_path = Path(__file__).resolve().parent

drawings_path = posts_path / "drawings"
books_path = posts_path / "books"
comics_path = posts_path / "comics"

drawings_output = posts_path / "drawings.json"
books_output = posts_path / "books.json"
comics_output = posts_path / "comics.json"

image_extensions = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".avif"
}

# ====================
# DRAWINGS
# ====================

def parse_date(filename):
    date = filename.split("@", 1)[1]
    date = date.rsplit(".", 1)[0]

    return datetime.strptime(
        date,
        "%d-%b-%Y"
    )


drawings_manifest = {}

for category in drawings_path.iterdir():

    if not category.is_dir():
        continue

    files = [
        file
        for file in category.iterdir()
        if file.is_file()
        and file.suffix.lower() in image_extensions
    ]

    thumbnail_path = category / "thumbnail"

    thumbnails = []

    if thumbnail_path.is_dir():
        thumbnails = [
            file
            for file in thumbnail_path.iterdir()
            if file.is_file()
            and file.suffix.lower() in image_extensions
        ]

    category_data = []

    for file in files:

        filename = file.stem

        parts = filename.split("@", 1)

        name = parts[0]

        thumbnail = None

        for thumb in thumbnails:
            if thumb.stem == name:
                thumbnail = thumb.name
                break

        category_data.append({
            "file": file.name,
            "thumbnail": thumbnail
        })

    category_data.sort(
        key=lambda item: parse_date(item["file"]),
        reverse=True
    )

    drawings_manifest[category.name] = category_data


drawings_manifest = dict(sorted(drawings_manifest.items()))

with drawings_output.open("w", encoding="utf-8") as file:
    json.dump(
        drawings_manifest,
        file,
        indent=2,
        ensure_ascii=False
    )
    file.write("\n")


# ====================
# BOOKS
# ====================

books_manifest = {}

for folder in books_path.iterdir():

    if not folder.is_dir():
        continue

    cover = None

    for file in folder.iterdir():
        if (
            file.is_file()
            and file.stem.lower() == "cover"
            and file.suffix.lower() in image_extensions
        ):
            cover = file.name
            break

    books_manifest[folder.name] = {
        "cover": cover
    }


with books_output.open("w", encoding="utf-8") as file:
    json.dump(
        books_manifest,
        file,
        indent=2,
        ensure_ascii=False
    )
    file.write("\n")


# ====================
# COMICS
# ====================

comics_manifest = {}

for folder in comics_path.iterdir():

    if not folder.is_dir():
        continue

    cover = None

    for file in folder.iterdir():
        if (
            file.is_file()
            and file.stem.lower() == "cover"
            and file.suffix.lower() in image_extensions
        ):
            cover = file.name
            break

    comics_manifest[folder.name] = {
        "cover": cover
    }


with comics_output.open("w", encoding="utf-8") as file:
    json.dump(
        comics_manifest,
        file,
        indent=2,
        ensure_ascii=False
    )
    file.write("\n")


print("Successfully generated:")
print(drawings_output)
print(books_output)
print(comics_output)