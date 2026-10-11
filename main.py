from pathlib import Path
import shutil

def organise_files(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")

    if not folder.is_dir():
        raise NotADirectoryError(f"Not a folder: {folder}")

    organised_count = 0

    for file in folder.iterdir():
        if not file.is_file():
            continue

        if file.name == "main.py" or file.name == "README.md":
            continue

        if not file.suffix:
            continue

        extension = file.suffix.lower().lstrip(".")
        target_folder = folder / extension
        target_folder.mkdir(exist_ok=True)

        destination = target_folder / file.name

        if destination.exists():
            continue

        shutil.move(str(file), str(destination))
        organised_count += 1

    return organised_count

if __name__ == "__main__":
    path = input("Enter the folder path to organise: ").strip().strip('"')

    try:
        count = organise_files(path)
        print(f"Successfully organised {count} file(s).")
    except (FileNotFoundError, NotADirectoryError) as error:
        print(f"Error: {error}")


