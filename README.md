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
