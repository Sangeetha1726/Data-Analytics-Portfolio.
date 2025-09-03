CREATE TABLE credit_card_transactions (
    transaction_id INT PRIMARY KEY,
    transaction_date DATE,
    customer_id INT,
    amount DECIMAL(10,2),
    merchant VARCHAR(100),
    location VARCHAR(100),
    is_fraud BIT
);

INSERT INTO credit_card_transactions VALUES
(1, '2025-07-01', 101, 250.50, 'Amazon', 'Chennai', 0),
(2, '2025-07-02', 102, 400.00, 'Flipkart', 'Mumbai', 0),
(3, '2025-07-03', 101, 1500.00, 'Gold Store', 'Delhi', 1),
(4, '2025-07-04', 103, 200.00, 'Grocery', 'Chennai', 0),
(5, '2025-07-04', 104, 10.00, 'Food Truck', 'Kolkata', 1),
(6, '2025-07-05', 102, 750.00, 'Electronics', 'Bangalore', 0),
(7, '2025-07-05', 105, 3000.00, 'Jewelry', 'Chennai', 1),
(8, '2025-07-06', 106, 500.00, 'Apparel', 'Mumbai', 0),
(9, '2025-07-06', 107, 20.00, 'Tea Shop', 'Chennai', 0),
(10, '2025-07-07', 108, 9000.00, 'Luxury Cars', 'Delhi', 1);


select * from credit_card_transactions

-- 1. Total Transactions
SELECT COUNT(*) AS TotalTransactions
FROM credit_card_transactions;

-- 2. Total Fraud Transactions
SELECT COUNT(*) AS FraudTransactions
FROM credit_card_transactions
WHERE is_fraud = 1;

-- 3. Fraud Percentage
SELECT 
    CAST(COUNT(CASE WHEN is_fraud = 1 THEN 1 END) * 100.0 / COUNT(*) AS DECIMAL(10,2)) AS FraudPercentage
FROM credit_card_transactions;

-- 4. Fraud by Location
SELECT 
    location,
    COUNT(*) AS TotalTransactions,
    SUM(CASE WHEN is_fraud = 1 THEN 1 ELSE 0 END) AS FraudTransactions,
    CAST(SUM(CASE WHEN is_fraud = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS DECIMAL(10,2)) AS FraudRate
FROM credit_card_transactions
GROUP BY location
ORDER BY FraudRate DESC;

-- 5. Fraud by Merchant
SELECT 
    merchant,
    COUNT(*) AS TotalTransactions,
    SUM(CASE WHEN is_fraud = 1 THEN 1 ELSE 0 END) AS FraudTransactions,
    CAST(SUM(CASE WHEN is_fraud = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS DECIMAL(10,2)) AS FraudRate
FROM credit_card_transactions
GROUP BY merchant
ORDER BY FraudRate DESC;

-- 6. Daily Fraud Trend
SELECT 
    transaction_date,
    COUNT(*) AS TotalTransactions,
    SUM(CASE WHEN is_fraud = 1 THEN 1 ELSE 0 END) AS FraudTransactions
FROM credit_card_transactions
GROUP BY transaction_date
ORDER BY transaction_date;

-- 7. High-Value Fraud Transactions (Threshold > 1000)
SELECT *
FROM credit_card_transactions
WHERE is_fraud = 1 AND amount > 1000
ORDER BY amount DESC;