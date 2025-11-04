SELECT 
    s.SaleID      AS SaleID,
    s.ProductID   AS ProductID,
    p.ProductName AS ProductName,
    p.Category    AS Category,
    p.UnitPrice   AS UnitPrice,
    s.CustomerID  AS CustomerID,
    c.CustomerName AS CustomerName,
    c.Gender      AS Gender,
    c.Age         AS Age,
    r.RegionName  AS Region,
    s.Quantity    AS Quantity,
    s.SaleDate    AS SaleDate,
    s.TotalAmount AS TotalAmount
FROM Sales s
LEFT JOIN Products p ON s.ProductID = p.ProductID
LEFT JOIN Customers c ON s.CustomerID = c.CustomerID
LEFT JOIN Regions r ON c.RegionID = r.RegionID;
