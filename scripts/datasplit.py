'''
import os

for split in ["val", "test"]:
    os.makedirs(f"dataset/images/{split}", exist_ok=True)
    os.makedirs(f"dataset/labels/{split}", exist_ok=True)

print("Folders created")
'''

'''
import os
import random
import shutil

images_path = "dataset/images/train"
labels_path = "dataset/labels/train"

images = os.listdir(images_path)
images = [img for img in images if img.endswith((".jpg", ".png"))]

random.shuffle(images)

total = len(images)

train_split = int(0.7 * total)
val_split = int(0.85 * total)

train_files = images[:train_split]
val_files = images[train_split:val_split]
test_files = images[val_split:]

def move_files(file_list, split):
    for img in file_list:
        label = img.rsplit(".", 1)[0] + ".txt"

        # move image
        shutil.move(
            os.path.join(images_path, img),
            f"dataset/images/{split}/{img}"
        )

        # move label
        shutil.move(
            os.path.join(labels_path, label),
            f"dataset/labels/{split}/{label}"
        )

move_files(val_files, "val")
move_files(test_files, "test")

print("Dataset split complete")

'''
#verify
import os
for split in ["train", "val", "test"]:
    img_count = len(os.listdir(f"dataset/images/{split}"))
    label_count = len(os.listdir(f"dataset/labels/{split}"))
    print(split, "Images:", img_count, "Labels:", label_count)
