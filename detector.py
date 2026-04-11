from ultralytics import YOLO
import sqlite3
import re
import cv2
import os

model = YOLO("models/machineparts.pt")



def normalize(text):
    return re.sub(r"\s+", "", text.lower())
CLASS_NAME_MAPPING = {
    normalize("Digital Temperature Controller Module"):
        "Digital Temperature Controller CS 3 H",

    normalize("Permanent Magnetic DC Motor"):
        "Permanent Magnetic DC Motor 90 V",

    normalize("Hand Sealer Controller Module w/o CT"):
        "Hand Sealer Control Module W/o CT"
}

def get_part_details(part_name):
    normalized_input = normalize(part_name)

     #Applying mapping safely
    mapped_name = CLASS_NAME_MAPPING.get(
        normalized_input,
        part_name
    )

    conn = sqlite3.connect("database/part_details.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT part_name, cost_price, stock
        FROM parts_details
    """)
    rows = cursor.fetchall()
    conn.close()

    for name, price, stock in rows:
        if normalize(name) == normalize(mapped_name):
            return name, price, stock

    return None


def detect(image_path):
    results = model(image_path, conf =0.90)
    annotated = results[0].plot()

    # Save annotated image
    output_path = os.path.join("static", "result.jpg")
    cv2.imwrite(output_path, annotated)

    detections = []
     
    for box in results[0].boxes:
        CONF_THRESHOLD = 0.90
                     
        confidence = float(box.conf[0])
        if confidence < CONF_THRESHOLD:
            continue
        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        part_data = get_part_details(class_name)
        part_data = get_part_details(class_name)
        if part_data:
             display_name = part_data[0]   
        else:
             display_name = class_name

        detections.append({
            "class": display_name,
            "confidence": round(confidence, 3),
            "details": part_data
        })

    return detections, output_path
