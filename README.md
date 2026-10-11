# File Organiser Automation

A Python automation project that organises files into separate folders based on their file extensions.

## Features

- Automatically sorts files by extension.
- Creates folders for file types such as JPG, PDF, TXT, and more.
- Skips files without extensions.
- Prevents overwriting files when a duplicate filename already exists.
- Handles invalid folder paths.
- Includes automated unit tests.

## Technologies Used

- Python
- pathlib
- shutil
- unittest

## Project Structure

```text
FileOrganiser/
├── main.py
├── README.md
└── tests/
    └── test_main.py
```

## How to Run

1. Install Python 3 if it is not already installed.
2. Open a terminal in the project directory.
3. Run the application:

```bash
python main.py
```

4. Enter the path of the folder you want to organise when prompted.

**Tip:** Test the application on a sample folder before using it on important files.

## Run Automated Tests

Run the following command from the project directory:

```bash
python -m unittest discover -s tests -v
```

The tests cover file organisation, invalid folder paths, empty folders, and files without extensions.

## Learning Outcomes

- File handling and directory management
- Python functions and exception handling
- Automated testing with `unittest`
- Working with filesystem paths using `pathlib`

## Author

Tauseem Shaikh