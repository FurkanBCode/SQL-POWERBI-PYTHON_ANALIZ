import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import os

conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-I5017OB\\SQLEXPRESS01;'
    'Database=RetailSalesDB;'
    'Trusted_Connection=yes;'
)

query = """
SELECT 
    s.SaleID,
    s.ProductID,
    p.ProductName,
    p.Category,
    p.UnitPrice,
    s.CustomerID,
    c.CustomerName,
    c.Gender,
    c.Age,
    r.RegionName AS Region,
    s.Quantity,
    s.SaleDate,
    s.TotalAmount
FROM Sales s
LEFT JOIN Products p ON s.ProductID = p.ProductID
LEFT JOIN Customers c ON s.CustomerID = c.CustomerID
LEFT JOIN Regions r ON c.RegionID = r.RegionID;
"""

df = pd.read_sql(query, conn)
conn.close()

os.makedirs("Retail_Sales_Analytics_Plots", exist_ok=True)

# 1️⃣ Bölgelere göre toplam satış
plt.figure(figsize=(8,5))
df.groupby("Region")["TotalAmount"].sum().sort_values(ascending=False).plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Bölgelere Göre Toplam Satış")
plt.xlabel("Bölge")
plt.ylabel("Toplam Satış (₺)")
plt.tight_layout()
plt.savefig("Retail_Sales_Analytics_Plots/bolgelere_gore_satislar.png")
plt.close()

# 2️⃣ Cinsiyete göre satış dağılımı
plt.figure(figsize=(6,6))
df.groupby("Gender")["TotalAmount"].sum().plot(kind="pie", autopct="%1.1f%%", startangle=90, colors=["#00BFFF", "#FF69B4"])
plt.title("Cinsiyete Göre Satış Dağılımı")
plt.ylabel("")
plt.tight_layout()
plt.savefig("Retail_Sales_Analytics_Plots/cinsiyete_gore_satislar.png")
plt.close()

# 3️⃣ Aylık satış trendi
df["Month"] = pd.to_datetime(df["SaleDate"]).dt.to_period("M")
plt.figure(figsize=(10,6))
df.groupby("Month")["TotalAmount"].sum().plot(kind="line", marker="o", color="orange")
plt.title("Aylık Satış Trendleri")
plt.xlabel("Ay")
plt.ylabel("Toplam Satış (₺)")
plt.grid(True)
plt.tight_layout()
plt.savefig("Retail_Sales_Analytics_Plots/aylik_satis_trendi.png")
plt.close()

# 4️⃣ En çok satılan ürünler
plt.figure(figsize=(10,6))
df.groupby("ProductName")["TotalAmount"].sum().nlargest(10).plot(kind="barh", color="lightgreen", edgecolor="black")
plt.title("En Çok Satılan 10 Ürün")
plt.xlabel("Toplam Satış (₺)")
plt.tight_layout()
plt.savefig("Retail_Sales_Analytics_Plots/en_cok_satilan_urunler.png")
plt.close()

print("✅ Grafikler başarıyla oluşturuldu ve 'Python/grafikler' klasörüne kaydedildi!")
