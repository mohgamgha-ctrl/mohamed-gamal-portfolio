-- Healthcare Billing & Patient Analysis Queries
SELECT 
    Specialty,
    COUNT(Patient_ID) AS Total_Patients,
    AVG(LOS_Days) AS Avg_Length_Of_Stay,
    AVG(Billing_Amount) AS Avg_Billing
FROM Hospital_Admissions
GROUP BY Specialty;

-- AdventureWorks Sales Trends Query
SELECT 
    SalesYear,
    ProductCategory,
    SUM(TotalRevenue) AS Total_Sales,
    COUNT(SalesOrderID) AS Order_Count
FROM FactSales
GROUP BY SalesYear, ProductCategory;