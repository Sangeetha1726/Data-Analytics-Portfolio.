import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# ============================
# 1. Connect to SQL Server
# ============================
try:
    # Replace "sql server" with your DSN name
    engine = create_engine("mssql+pyodbc://sql server")
    print("✅ Connection successful!")
except Exception as e:
    print("❌ Connection failed:", e)
    exit()

# ============================
# 2. Read SQL Table into Pandas
# ============================
query = "SELECT * FROM credit_card_transactions"
df = pd.read_sql(query, engine)
print("\n📊 First 5 Rows:\n", df.head().to_string())

# ============================
# 3. Fraud Analysis
# ============================
total_txn = len(df)
fraud_txn = df[df['is_fraud'] == 1].shape[0]
fraud_pct = round((fraud_txn / total_txn) * 100, 2)

fraud_by_location = df.groupby("location")['is_fraud'].agg(['count', 'sum'])
fraud_by_location['FraudRate(%)'] = round(
    (fraud_by_location['sum'] / fraud_by_location['count']) * 100, 2
)

fraud_by_merchant = df.groupby("merchant")['is_fraud'].agg(['count', 'sum'])
fraud_by_merchant['FraudRate(%)'] = round(
    (fraud_by_merchant['sum'] / fraud_by_merchant['count']) * 100, 2
)

daily_fraud = df.groupby("transaction_date")['is_fraud'].agg(['count', 'sum'])
daily_fraud['FraudRate(%)'] = round(
    (daily_fraud['sum'] / daily_fraud['count']) * 100, 2
)

high_value_fraud = df[(df['is_fraud'] == 1) & (df['amount'] > 1000)]

# ============================
# 4. Display Results
# ============================
print("\n📌 Fraud Summary Report")
print(f"Total Transactions: {total_txn}")
print(f"Fraud Transactions: {fraud_txn}")
print(f"Fraud Percentage: {fraud_pct}%\n")

print("🏙️ Fraud by Location:\n", fraud_by_location.to_string())
print("\n🏬 Fraud by Merchant:\n", fraud_by_merchant.to_string())
print("\n📅 Daily Fraud Trend:\n", daily_fraud.to_string())
print("\n💰 High Value Fraud Transactions:\n", high_value_fraud.to_string())

# ============================
# 5. Visualizations
# ============================

# Fraud by Location (Bar Chart)
plt.figure(figsize=(8, 5))
plt.bar(fraud_by_location.index, fraud_by_location['sum'], color='tomato')
plt.title("Fraud Count by Location")
plt.xlabel("Location")
plt.ylabel("Fraud Count")
plt.xticks(rotation=45)
plt.show()

# Fraud by Merchant (Top 10)
top_merchants = fraud_by_merchant.sort_values("sum", ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_merchants.index, top_merchants['sum'], color='orange')
plt.title("Top 10 Merchants by Fraud Count")
plt.xlabel("Fraud Count")
plt.ylabel("Merchant")
plt.gca().invert_yaxis()
plt.show()

# Daily Fraud Trend (Line Chart)
plt.figure(figsize=(10, 5))
plt.plot(daily_fraud.index, daily_fraud['sum'], marker='o', linestyle='-', color='blue')
plt.title("Daily Fraud Trend")
plt.xlabel("Date")
plt.ylabel("Fraud Count")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Fraud vs Non-Fraud (Pie Chart)
fraud_vs_nonfraud = [fraud_txn, total_txn - fraud_txn]
labels = ["Fraud", "Non-Fraud"]
colors = ["red", "green"]
plt.figure(figsize=(6, 6))
plt.pie(fraud_vs_nonfraud, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title("Fraud vs Non-Fraud Transactions")
plt.show()
