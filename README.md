# 📊 Sales Analytics Dashboard — Python Data Analyst Portfolio Project

An interactive **Sales Analytics Dashboard** built with Python, Pandas, NumPy, Plotly, and Streamlit.

The project transforms retail sales data into an interactive dashboard that helps analyze **sales, profit, orders, units sold, product performance, regional performance, customer segments, payment modes, and monthly sales trends**.

---

## 🚀 Live Dashboard

**Streamlit App:** Add your deployed Streamlit URL here

Example:

`https://your-app-name.streamlit.app`

---

## 📌 Project Overview

This project was developed as a Data Analyst portfolio project to demonstrate an end-to-end analytics workflow using Python.

The workflow includes:

```text
Raw Sales Data
      ↓
Data Cleaning
      ↓
Data Transformation
      ↓
Exploratory Data Analysis
      ↓
Business Metrics
      ↓
Interactive Visualizations
      ↓
Streamlit Dashboard
```

The dashboard allows users to select a **date range** and dynamically analyze the sales data for the selected period.

---

## 🎯 Business Objectives

The project focuses on answering practical business questions such as:

- What are the total sales and total profit?
- How many orders were generated?
- How many units were sold?
- What is the overall profit margin?
- How do sales change month by month?
- Which product categories generate the most sales?
- How do different customer segments contribute to sales?
- Which payment modes generate the most sales?
- How do sales and profit vary across regions?
- Which products generate the highest sales?
- What is the relationship between sales and profit?
- How does performance change when a different date range is selected?

---

# 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data analysis and application development |
| Pandas | Data cleaning, transformation and aggregation |
| NumPy | Numerical calculations |
| Plotly Express | Interactive charts and visualizations |
| Streamlit | Interactive web dashboard |
| Jupyter Notebook | Data analysis and exploration |
| GitHub | Version control and portfolio hosting |

---

# 📂 Project Structure

```text
Retail sales analysis project/
│
├── app.py
├── python_data_analyst_sales_project.csv
├── python_data_analyst_sales_project_cleaned.csv
├── requirements.txt
├── Retail sales analysis project using Python.ipynb
└── README.md
```

### File Description

**`app.py`**

Main Streamlit application containing the dashboard logic, filters, KPIs, charts, and data tables.

**`python_data_analyst_sales_project.csv`**

Original sales dataset used for the project.

**`python_data_analyst_sales_project_cleaned.csv`**

Cleaned dataset used by the Streamlit application.

**`Retail sales analysis project using Python.ipynb`**

Jupyter Notebook containing the Python analysis workflow.

**`requirements.txt`**

Python libraries required to run the dashboard.

---

# 🧹 Data Preparation

The Streamlit application performs several data preparation steps before analysis.

### Duplicate records

Duplicate rows are removed:

```python
df = df.drop_duplicates()
```

### Date conversion

The order date is converted into a proper datetime format:

```python
df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)
```

### Numeric conversion

The following fields are converted to numeric values:

```text
Sales
Profit
Quantity
Unit_Price
```

### Missing values

Missing values are handled using:

- Median replacement for `Sales`
- Median replacement for `Profit`
- Default value `1` for missing `Quantity`

Example:

```python
df["Sales"] = df["Sales"].fillna(df["Sales"].median())
df["Profit"] = df["Profit"].fillna(df["Profit"].median())
df["Quantity"] = df["Quantity"].fillna(1)
```

### Monthly analysis

A monthly field is created from the order date:

```python
df["Month_Year"] = df["Order_Date"].dt.to_period("M").astype(str)
```

This is used to analyze monthly sales trends.

---

# 📊 Dashboard KPIs

The dashboard displays five primary KPIs.

### 1. Total Sales

Total sales generated within the selected date range.

```python
sales = data["Sales"].sum()
```

### 2. Total Profit

Total profit generated within the selected date range.

```python
profit = data["Profit"].sum()
```

### 3. Orders

Number of unique orders.

```python
orders = data["Order_ID"].nunique()
```

### 4. Units Sold

Total quantity sold.

```python
quantity = data["Quantity"].sum()
```

### 5. Profit Margin

Calculated as:

```text
Profit Margin = Total Profit / Total Sales × 100
```

Python implementation:

```python
margin = profit / sales * 100 if sales else 0
```

---

# 📅 Interactive Date Filter

The dashboard contains a date-range filter in the sidebar.

Users can select:

```text
Start Date → End Date
```

The dashboard then recalculates all KPIs and visualizations for the selected period.

Example:

```text
01/01/2023 → 31/12/2025
```

---

# 📈 Dashboard Pages

The application contains four major sections.

---

## 1. 📈 Overview

The Overview section contains:

### Monthly Sales Trend

A line chart showing how sales change across months.

### Sales by Category

A bar chart comparing sales across product categories.

### Sales by Segment

A donut chart showing sales contribution by customer segment.

### Sales by Payment Mode

A bar chart comparing sales across payment methods.

---

## 2. 🌍 Regional Analysis

The Regional Analysis section contains:

### Sales by Region

Compares sales generated across regions.

### Profit by Region

Compares profit generated across regions.

### Regional Performance Table

Provides summarized sales and profit by region.

---

## 3. 🛍️ Product Analysis

The Product Analysis section contains:

### Top 10 Products by Sales

Displays the ten products with the highest sales.

### Sales vs Profit

A scatter plot used to explore the relationship between sales and profit.

The visualization also includes:

- Product
- Region
- Segment
- Quantity
- Category

### Product Performance Table

Provides:

- Sales
- Profit
- Quantity
- Orders

for each product.

---

## 4. 📋 Data

The Data section provides the filtered dataset directly inside the dashboard.

Users can:

- View filtered records
- Review individual transactions
- Download the filtered data as a CSV file

---

# 📐 Key Calculations

### Total Sales

```python
sales = data["Sales"].sum()
```

### Total Profit

```python
profit = data["Profit"].sum()
```

### Unique Orders

```python
orders = data["Order_ID"].nunique()
```

### Units Sold

```python
quantity = data["Quantity"].sum()
```

### Profit Margin

```python
margin = profit / sales * 100 if sales else 0
```

---

# 💡 Business Analysis Framework

The dashboard can be used to investigate four major areas:

### Revenue

Analyze:

- Total sales
- Monthly sales
- Category sales
- Regional sales
- Product sales

### Profitability

Analyze:

- Total profit
- Profit margin
- Regional profit
- Sales vs profit

### Customer / Sales Segmentation

Analyze:

- Customer segments
- Payment modes
- Regional performance

### Product Performance

Analyze:

- Top-selling products
- Product sales
- Product profit
- Quantity sold
- Number of orders

---

# 💻 How to Run the Project Locally

## Step 1 — Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/retail-sales-analytics-dashboard.git
```

Move into the project:

```bash
cd retail-sales-analytics-dashboard
```

---

## Step 2 — Install dependencies

```bash
pip install -r requirements.txt
```

The project requires:

```text
streamlit
pandas
numpy
plotly
```

---

## Step 3 — Run Streamlit

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

# ☁️ Streamlit Deployment

The dashboard can be deployed using **Streamlit Community Cloud**.

Required repository structure:

```text
retail-sales-analytics-dashboard/
│
├── app.py
├── python_data_analyst_sales_project_cleaned.csv
├── requirements.txt
└── README.md
```

Set the Streamlit entry point to:

```text
app.py
```

---

# 📸 Dashboard Preview

Add your dashboard screenshot here:

```markdown
![Sales Analytics Dashboard](dashboard.png)
```

Recommended repository structure after adding the screenshot:

```text
retail-sales-analytics-dashboard/
│
├── app.py
├── python_data_analyst_sales_project_cleaned.csv
├── requirements.txt
├── README.md
└── dashboard.png
```

---

# 🧠 Data Analyst Skills Demonstrated

This project demonstrates:

### Python

- Pandas
- NumPy
- Functions
- Data cleaning
- Data transformation
- GroupBy
- Aggregation
- Date/time analysis

### Data Analysis

- KPI calculation
- Trend analysis
- Category analysis
- Regional analysis
- Product analysis
- Profitability analysis
- Segmentation

### Data Visualization

- Line charts
- Bar charts
- Donut charts
- Scatter plots
- Interactive filtering

### Dashboard Development

- Streamlit
- Interactive date filtering
- KPI cards
- Dynamic charts
- Data tables
- CSV export

---

# 📌 Project Highlights

- Built an interactive sales analytics dashboard using Streamlit.
- Processed and analyzed retail sales data using Pandas and NumPy.
- Created dynamic KPIs for sales, profit, orders, units sold, and profit margin.
- Added date-based filtering for interactive analysis.
- Developed interactive Plotly visualizations for trends, categories, segments, payment modes, regions, and products.
- Added filtered-data export functionality.
- Designed the project as an end-to-end Data Analyst portfolio project.

---

# 🔗 Portfolio Links

**Live Dashboard:** Add Streamlit URL

**GitHub Repository:** Add GitHub URL

**LinkedIn:** Add LinkedIn URL

---

# 👨‍💻 Author

**Tarun Sahani**

Data Analyst | Python | SQL | Excel | Power BI | Streamlit

---

## ⭐ If you find this project useful

Feel free to explore the repository and connect with me on LinkedIn.
