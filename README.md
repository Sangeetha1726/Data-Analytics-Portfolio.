# Data-Analytics-Portfolio.

# 🕵️ Credit Card Fraud Analysis (Python + SQL Server)

A small analytics project that reads transactions from **SQL Server**, calculates fraud metrics, and generates charts with **Matplotlib**.

## ✨ What’s inside
- Fraud percentage and counts
- Fraud by **location** and **merchant**
- **Daily** fraud trend
- **High-value** frauds (> 1000)
- Charts saved in `screenshots/`

## 🧰 Tech
Python (pandas, numpy, matplotlib, sqlalchemy, pyodbc) + SQL Server

## 🚀 How to run
1. Ensure an ODBC DSN exists (e.g., `sql server`) that points to your SQL Server.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

