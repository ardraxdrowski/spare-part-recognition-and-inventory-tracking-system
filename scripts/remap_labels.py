import os

folders = [
    r"C:\Users\admin\Downloads\Control board.v3i.yolov8\train\labels",
    r"C:\Users\admin\Downloads\Control board.v3i.yolov8\valid\labels",
    r"C:\Users\admin\Downloads\Control board.v3i.yolov8\test\labels",
]

for label_dir in folders:
    for file in os.listdir(label_dir):
        path = os.path.join(label_dir, file)

        with open(path, "r") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            parts = line.strip().split()
            parts[0] = "4"  # NEW CLASS ID
            new_lines.append(" ".join(parts))

        with open(path, "w") as f:
            f.write("\n".join(new_lines))

print("✅ Remapping complete")
