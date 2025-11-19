# Customer Shopping Behavior Analysis

## 📊 Overview
This project analyzes customer shopping behavior to uncover insights about spending patterns, demographics, and purchasing preferences.
It demonstrates the complete data analytics workflow from cleaning and preparing data in Python, storing and analyzing it in PostgreSQL, to visualizing insights through Power BI and summarizing key findings in Gamma.
<img width="1345" height="735" alt="image" src="https://github.com/user-attachments/assets/4d04bc46-88ed-4fc7-b5dc-f8e7356ead5c" />

---

## 📁 Dataset

**Source:** Customer shopping behavior dataset (customer_shopping_behavior.csv)

**Size:** 3900 records

**Type:** Retail transaction data

**Key Fields:**

Customer_ID, Gender, Age, Category, Item_Purchased, Purchase_Amount, Review_Rating, Subscription_Status, Shipping_Type, etc.

---

## 🧰 Tools & Technologies

| Tool                           | Purpose                                   |
| ------------------------------ | ----------------------------------------- |
| **Python (Pandas, NumPy)**     | Data loading, cleaning, and preprocessing |
| **PostgreSQL**                 | SQL-based querying and data storage       |
| **SQLAlchemy**                 | Python–PostgreSQL connection              |
| **Power BI**                   | Interactive dashboard and visualizations  |
| **Gamma**                      | Automated presentation of insights        |
| **VS Code** | Development environment                   |

---

## ⚙️ Project Workflow

1. **Data Cleaning (Python)**

**Script:** customer_shopping_behaviour.py

**Key steps:**

- Load dataset using pandas

- Handle missing values (imputed median Review Rating by product category)

- Rename columns to snake_case for consistency

**Create new fields:**

- age_group (Young Adult, Adult, Middle Aged, Senior)

- purchase_frequency_days (mapped from text frequency)

- Drop redundant columns (promo_code_used)

- Export cleaned dataset for SQL upload

**2. Database Integration (PostgreSQL)**

**Script**: load_to_postgres.py

- Connection made via SQLAlchemy

- Credentials defined for PostgreSQL (username, password, host, port, database)

- Data uploaded into table: customer within database: customer_behaviour

**3. SQL Analysis**

**File:** customer_behaviour_SQL_queries.sql

- **Key analytical queries**:

- Revenue by Gender – Compare male vs. female customer revenue

- Discount Usage vs. Spending – Identify customers who used discounts but spent above average

- Top Rated Products – Top 5 products by average review rating

- Shipping Type Comparison – Compare average purchase amount for Standard vs. Express

- Subscriber Analysis – Compare total revenue and average spend of subscribers vs. non-subscribers

- Discount Rate by Product – Identify products most often purchased with discounts

- Customer Segmentation – Segment customers into New, Returning, and Loyal

- Top Products per Category – Find top 3 purchased products within each category

- Repeat Buyers & Subscription – Analyze subscription rates among repeat buyers

- Revenue by Age Group – Compare spending across customer age groups

**4. Dashboard (Power BI)**

Connected Power BI to PostgreSQL / cleaned CSV

Open customer_behavior_dashboard.pbix

**5. Presentation (Gamma)**

Key insights summarized into a Gamma-powered presentation

Included visuals from Power BI and highlights from SQL results

Structured for storytelling and executive reporting

---

## 📈 Key Insights

- Female customers generated slightly higher total revenue than males.

- Discounted purchases often came from high-value customers, indicating effective promotional impact.

- Express shipping customers showed higher spending behavior.

- Loyal customers (10+ purchases) contributed the largest share of total revenue.

- Adults and Middle-Aged groups were the highest-spending segments.

---

## 💡 Business Recommendations

- **Targeted Promotions:**
Continue offering targeted discounts to high-value and loyal customers — they respond positively without hurting revenue.

- **Subscription Program Expansion:**
Subscribers spend more on average; increasing incentives for non-subscribers could boost long-term retention.

- **Shipping Strategy Optimization:**
Since express shipping users tend to spend more, bundle express delivery with premium loyalty plans to drive upselling.

- **Product Focus:**
Prioritize inventory and marketing around top-rated and frequently purchased products to maximize profitability.

- **Customer Segmentation Marketing:**
Create separate campaigns for New, Returning, and Loyal customers to improve engagement and conversion rates.

- **Age-Based Personalization:**
Tailor marketing strategies to Adult and Middle-Aged customers — the two groups driving most of the revenue.

---

## 🚀 How to Run

1. Clone Repository
   
git clone
https://github.com/jinalkhona01-collab/customer-trends-data-analysis-SQL-Python-PowerBI.git

cd customer-trends-data-analysis-SQL-Python-PowerBI

2. Install Dependencies
   
pip install -r requirements.txt

3. Clean and Prepare Data
   
python customer_shopping_behaviour.py

4. Upload Data to PostgreSQL
   
python load_to_postgres.py

5. Run SQL Queries

Execute queries from customer_analysis.sql using pgAdmin or DBeaver.

6. View Dashboard

Open customer_dashboard.pbix in Power BI.

7. View Presentation

Access the Gamma presentation - open Customer-Shopping-Behavior-Analysis.pptx.

---

## About Me
Hi there! I'm ***Jinal Mahesh Khona***. I’m on a mission to share and gain knowledge and make working with data enjoyable and engaging!

## ☕ Stay Connected

Let's stay in touch! Feel free to connect with me on

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)][(https://www.linkedin.com/in/jinal-khona-84835523a/)]

Email: jinal.khona01@gmail.com
