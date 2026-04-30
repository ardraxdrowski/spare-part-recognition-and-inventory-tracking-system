import cv2
import os
import numpy as np

dataset_root = "../generated_datasets"

for condition in os.listdir(dataset_root):

    img_folder = os.path.join(dataset_root, condition, "images")
    label_folder = os.path.join(dataset_root, condition, "labels")

    contrasts = []

    for label_file in os.listdir(label_folder):

        label_path = os.path.join(label_folder, label_file)
        img_name = label_file.replace(".txt", ".jpg")
        img_path = os.path.join(img_folder, img_name)

        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE).astype(np.float32)

        h, w = image.shape

        with open(label_path) as f:
            lines = f.readlines()

        for line in lines:

            parts = line.strip().split()
            xc, yc, bw, bh = map(float, parts[1:])

            x1 = int((xc - bw/2) * w)
            y1 = int((yc - bh/2) * h)
            x2 = int((xc + bw/2) * w)
            y2 = int((yc + bh/2) * h)

            crop = image[y1:y2, x1:x2]

            if crop.size == 0:
                continue

            Imax = float(np.max(crop))
            Imin = float(np.min(crop))

            if (Imax + Imin) > 0:
                C = (Imax - Imin) / (Imax + Imin)
                contrasts.append(C)

    avg_contrast = np.mean(contrasts)

    print(condition, "Local Michelson Contrast:", round(avg_contrast,3))