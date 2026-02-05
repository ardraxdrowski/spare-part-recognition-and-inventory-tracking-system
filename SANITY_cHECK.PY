import os

for split in ["train", "val", "test"]:
    img = len(os.listdir(f"dataset/images/{split}"))
    lab = len(os.listdir(f"dataset/labels/{split}"))
    print(split, img, lab)
