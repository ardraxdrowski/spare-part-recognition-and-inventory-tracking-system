import cv2
import os
import numpy as np

INPUT_DIR = "../../dataset/images/val"
OUTPUT_ROOT = "../generated_datasets"

os.makedirs(OUTPUT_ROOT, exist_ok=True)

# experiment levels
contrast_levels = [1.0, 0.8, 0.6, 0.4]
brightness_levels = [-60, -30, 0, 30]
noise_levels = [0, 10, 20, 30]

for img_name in os.listdir(INPUT_DIR):

    img_path = os.path.join(INPUT_DIR, img_name)
    img = cv2.imread(img_path)

    # ---------- CONTRAST ----------
    for a in contrast_levels:
        out_dir = f"{OUTPUT_ROOT}/contrast_{a}"
        os.makedirs(out_dir, exist_ok=True)

        new = cv2.convertScaleAbs(img, alpha=a, beta=0)

        cv2.imwrite(os.path.join(out_dir, img_name), new)

    # ---------- BRIGHTNESS ----------
    for b in brightness_levels:
        out_dir = f"{OUTPUT_ROOT}/brightness_{b}"
        os.makedirs(out_dir, exist_ok=True)

        new = cv2.convertScaleAbs(img, alpha=1, beta=b)

        cv2.imwrite(os.path.join(out_dir, img_name), new)

    # ---------- LOW LIGHT ----------
    low = cv2.convertScaleAbs(img, alpha=0.4, beta=-40)

    out_dir = f"{OUTPUT_ROOT}/low_light"
    os.makedirs(out_dir, exist_ok=True)

    cv2.imwrite(os.path.join(out_dir, img_name), low)

    # ---------- GAUSSIAN NOISE ----------
    for n in noise_levels:

        out_dir = f"{OUTPUT_ROOT}/noise_{n}"
        os.makedirs(out_dir, exist_ok=True)

        noise = np.random.normal(0, n, img.shape)
        noisy = img + noise
        noisy = np.clip(noisy,0,255).astype(np.uint8)

        cv2.imwrite(os.path.join(out_dir, img_name), noisy)

print("Adverse datasets generated")