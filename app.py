from flask import Flask, render_template, request, jsonify
import os
from detector import detect
import sqlite3
import pandas as pd
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
from flask import jsonify
import sqlite3

@app.route("/place_order", methods=["POST"])
def place_order():
    part_name = request.form.get("part_name")
    quantity = int(request.form.get("quantity", 1))

    conn = sqlite3.connect("database/part_details.db")
    cursor = conn.cursor()

    #Check current stock
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

    #Decrease stock
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

@app.route("/save_replacement", methods=["POST"])
def save_replacement():
    print("SAVE REPLACEMENT ROUTE CALLED")

    part_name = request.form.get("part_name")
    quantity = int(request.form.get("quantity"))
    date = request.form.get("date")
    reason = request.form.get("reason")
    warranty_status = request.form.get("warranty_status")

    criticality = "Critical"

    # -------- Get current stock from database --------
    conn = sqlite3.connect("database/part_details.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT stock FROM parts_details WHERE part_name = ?",
        (part_name,)
    )

    row = cursor.fetchone()
    conn.close()

    current_stock = row[0] if row else 0

    # -------- Determine stock level --------
    if current_stock > 10:
        stock_level = "High"
    elif current_stock >= 5:
        stock_level = "Medium"
    else:
        stock_level = "Low"

    # -------- Recommendation logic --------
    recommendation_matrix = {
        ("Critical", "Low"): "Order immediately",
        ("Critical", "Medium"): "Maintain reserve stock",
        ("Critical", "High"): "No action",
        ("Semi-critical", "Low"): "Order soon",
        ("Semi-critical", "Medium"): "Monitor stock",
        ("Semi-critical", "High"): "No action",
        ("Non-critical", "Low"): "Order if required",
        ("Non-critical", "Medium"): "No action",
        ("Non-critical", "High"): "No action",
    }

    action = recommendation_matrix.get((criticality, stock_level), "No action")

    file_path = "replacement_log.xlsx"

    # -------- Read existing Excel --------
    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
        sno = len(df) + 1
    else:
        df = pd.DataFrame()
        sno = 1

    new_data = {
        "sno": sno,
        "date": date,
        "part_name": part_name,
        "quantity": quantity,
        "reason": reason,
        "warranty_status": warranty_status,
        "current_stock": current_stock,   # ⭐ NEW COLUMN
        "stock_level": stock_level,
        "action": action
    }

    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

    df.to_excel(file_path, index=False)

    return jsonify({"status": "success"})
     
if __name__ == "__main__":
    app.run(debug=True)
