# dataset split script - initial version
import os
import shutil

for split in ["val", "test"]:
    os.makedirs(f"dataset/images/{split}", exist_ok=True)
    os.makedirs(f"dataset/labels/{split}", exist_ok=True)

print("Folders created")
