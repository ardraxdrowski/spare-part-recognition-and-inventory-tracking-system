from ultralytics import YOLO
import cv2
import os

model = YOLO("models/machineparts.pt")

def detect(image_path):
    results = model(image_path, conf=0.50)
    annotated = results[0].plot()

    output_path = os.path.join("static", "result.jpg")
    cv2.imwrite(output_path, annotated)

    detections = []
    for box in results[0].boxes:
        confidence = float(box.conf[0])
        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        detections.append({
            "class": class_name,
            "confidence": round(confidence, 3),
            "details": None
        })

    return detections, output_path
