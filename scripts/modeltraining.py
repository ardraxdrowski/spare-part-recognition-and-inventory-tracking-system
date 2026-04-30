import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

from ultralytics import YOLO

model = YOLO("models/yolov8n.pt")  # base model

model.train(
    data="data.yaml",
    epochs=40,
    imgsz=640,
    batch=8
)
