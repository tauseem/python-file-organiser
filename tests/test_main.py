import unittest
import tempfile
from pathlib import Path

from main import organise_files

class TestFileOrganiser(unittest.TestCase):


    def test_organise_files_by_extension(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)

            (folder / "photo.jpg").write_text("image")
            (folder / "notes.txt").write_text("text")
            (folder / "resume.pdf").write_text("pdf")

            count = organise_files(folder)

            self.assertEqual(count, 3)
            self.assertTrue((folder / "jpg" / "photo.jpg").exists())
            self.assertTrue((folder / "txt" / "notes.txt").exists())
            self.assertTrue((folder / "pdf" / "resume.pdf").exists())

    def test_missing_folder_raises_error(self):
        with self.assertRaises(FileNotFoundError):
         organise_files("folder_that_does_not_exist_12345")

        if __name__ == "__main__":
            unittest.main()


    def test_empty_folder(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            count = organise_files(temp_dir)
            self.assertEqual(count, 0)

    def test_file_without_extension_is_skipped(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)
            file_path = folder / "myfile"
            file_path.write_text("sample")

            count = organise_files(folder)

            self.assertEqual(count, 0)
            self.assertTrue(file_path.exists())

