from ultralytics import YOLO
import cv2

model = YOLO("models/machineparts.pt")

results = model("imageuploads/IMG-20260106-WA0095.jpg")

# Get image with bounding boxes
annotated_frame = results[0].plot()

# Show image
cv2.imshow("Detection", annotated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

