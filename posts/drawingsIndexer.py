import json
from pathlib import Path

posts_path = Path(__file__).resolve().parent
drawings_path = posts_path / "drawings"
output_path = posts_path / "drawings.json"

print("Posts:    ", posts_path)
print("Drawings: ", drawings_path)
print("Output:   ", output_path)

image_extensions = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".avif"
}

manifest = {}

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
        date = parts[1] if len(parts) > 1 else None

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
        key=lambda item: item["file"].lower()
    )

    manifest[category.name] = category_data

manifest = dict(sorted(manifest.items()))

# be absolutely sure that it still exists
output_path.parent.mkdir(parents=True, exist_ok=True)

# start writing
with output_path.open("w", encoding="utf-8") as file:
    json.dump(
        manifest,
        file,
        indent=2,
        ensure_ascii=False
    )
    file.write("\n")

print()
print("Successfully generated:")
print(output_path)