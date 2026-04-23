from flask import Flask, render_template, request, jsonify
import os
from detector import detect
import sqlite3

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

@app.route("/place_order", methods=["POST"])
def place_order():
    part_name = request.form.get("part_name")
    quantity = int(request.form.get("quantity", 1))

    conn = sqlite3.connect("database/part_details.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT stock FROM parts_details WHERE part_name = ?",
        (part_name,)
    )
    row = cursor.fetchone()

    if not row:
        conn.close()
        return jsonify({"status": "error", "message": "Part not found"})

    current_stock = row[0] or 0
    if current_stock < quantity:
        conn.close()
        return jsonify({"status": "error", "message": "Insufficient stock"})

    cursor.execute(
        """
        UPDATE parts_details
        SET stock = stock - ?
        WHERE part_name = ?
        """,
        (quantity, part_name)
    )
    conn.commit()
    conn.close()
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
