# Spare Part Recognition & Smart Inventory Management System

This project is an AI-powered system designed to automate spare part identification and stock control for industrial packaging machines.

## Phase 1: Data-Driven Criticality Analysis
Prior to any development, we conducted a comprehensive data analysis of two years of field service data from a packaging machinery manufacturer.
The goal was to identify which spare parts were the most critical to target for automated recognition.

We applied the **Pareto Principle (80/20 Rule)** to identify the vital few components that contribute to the majority of machine failures and downtime.

### Criticality Index Formula
To rank the parts objectively, we calculated a **Criticality Index (CI)** for each spare part using a weighted scoring model:

\[CI = W_f \cdot F_{pct} + W_c \cdot C_{repl} + W_t \cdot T_{repl} + W_d \cdot D_{cont}\]

Where:
- \(F_{pct}\): Failure percentage (weight \(W_f = 0.35\))
- \(C_{repl}\): Cost of replacement (weight \(W_c = 0.20\))
- \(T_{repl}\): Replacement time (weight \(W_t = 0.15\))
- \(D_{cont}\): Downtime contribution (weight \(W_d = 0.30\))

Using this formula, we selected the top 5 most critical spare parts for dataset collection and model training.

## Phase 2: Dataset Configuration
We configured the initial dataset to label the first batch of critical spare parts:
- Digital Temperature Controller Module
- Permanent Magnetic DC Motor
- Hand Sealer Controller Module w/o CT

## Phase 3: Dataset Splitting & Preprocessing
To prepare the images for training, we developed data preparation pipelines to shuffle and split raw image uploads into training, validation, and testing sets using a 70/15/15 ratio.
This ensures proper evaluation metrics and prevents overfitting.

## Phase 4: Model Training
We trained a custom object detection model using **YOLOv8** (nano configuration) to locate and identify critical machine parts in real-time.

## Phase 5: Inventory Database Setup
An SQLite database (`part_details.db`) was introduced to map detected parts directly to operational metadata. This allows the system to look up pricing and current stock levels dynamically.

## Phase 6: YOLO Detection Bridge
We built the detection pipeline (`detector.py`) which acts as the bridge between the custom YOLO model and the SQLite database. It extracts class predictions and fetches corresponding database information.
