from flask import Flask, render_template, request
import os
from detector import detect

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        if file:
            path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(path)
            detections, result_image = detect(path)
            return render_template(
                "index.html",
                result_image=result_image,
                detections=detections
            )
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
