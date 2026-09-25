import json
from pathlib import Path

posts_path = Path(__file__).resolve().parent
books_path = posts_path / "books"
output_path = posts_path / "books.json"

image_extensions = {
    ".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"
}

manifest = {}

folders = [
    folder for folder in books_path.iterdir()
    if folder.is_dir()
]

for folder in folders:
    cover = None

    for file in folder.iterdir():
        if (
            file.is_file()
            and file.stem.lower() == "cover"
            and file.suffix.lower() in image_extensions
        ):
            cover = file.name
            break

    manifest[folder.name] = {
        "cover": cover
    }

with output_path.open("w", encoding="utf-8") as file:
    json.dump(manifest, file, indent=2, ensure_ascii=False)
    file.write("\n")

print(f"Updated: {output_path}")