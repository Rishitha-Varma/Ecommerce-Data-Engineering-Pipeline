-- 1. Calculate Total Revenue
SELECT
    SUM("TotalAmount") AS total_revenue
FROM online_retail;


-- 2. Calculate Monthly Revenue
SELECT
    "InvoiceYear",
    "InvoiceMonth",
    SUM("TotalAmount") AS monthly_revenue
FROM online_retail
GROUP BY "InvoiceYear", "InvoiceMonth"
ORDER BY "InvoiceYear", "InvoiceMonth";


-- 3. Find Top 10 Best-Selling Products
SELECT
    "StockCode",
    "Description",
    SUM("Quantity") AS total_quantity_sold
FROM online_retail
GROUP BY "StockCode", "Description"
ORDER BY total_quantity_sold DESC
LIMIT 10;


-- 4. Find Top 10 Customers
SELECT
    "CustomerID",
    SUM("TotalAmount") AS total_spent
FROM online_retail
WHERE "CustomerID" IS NOT NULL
GROUP BY "CustomerID"
ORDER BY total_spent DESC
LIMIT 10;


-- 5. Country-Wise Revenue
SELECT
    "Country",
    SUM("TotalAmount") AS total_revenue
FROM online_retail
GROUP BY "Country"
ORDER BY total_revenue DESC;


-- 6. Calculate Total Orders
SELECT
    COUNT(DISTINCT "InvoiceNo") AS total_orders
FROM online_retail;