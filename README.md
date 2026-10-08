# Customer Behavior Analysis
## About the Project
This project provides a comprehensive analysis of customer behavior to uncover key purchasing patterns, trends, and demographics. The analysis spans from raw data preprocessing to storage in a relational database, culminating in an interactive Power BI dashboard that offers actionable business insights.
## Technologies Used
 * Data Preprocessing: Python (Pandas), SQL (PostgreSQL)
 * Database Management: pgAdmin 4
 * Data Visualization: Power BI
## Key Features
1. Data Cleaning & Feature Engineering (Python & Pandas)
 * Handled missing values in the Review Rating column by imputing them with the median rating grouped by product category.
 * Standardized column names to maintain consistency and ease of use.
 * Created an Age Group column to categorize customers into distinct age brackets (Young Adult, Adult, Middle-Aged, Senior).
 * Mapped categorical Frequency of Purchases to numerical values representing days to enable quantitative analysis.
2. Database Operations (SQL & PostgreSQL)
 * Loaded the cleaned data into a PostgreSQL relational database.
 * Executed various analytical SQL queries to answer critical business questions, such as:
   * Revenue generation by gender.
   * Identifying customers who used discounts but still spent above the average purchase amount.
   * Pinpointing top-rated products and analyzing shipping types.
   * Segmenting customers into New, Returning, and Loyal based on purchase history.
3. Interactive Dashboard (Power BI)
 * Built an intuitive dashboard visualizing key performance indicators (KPIs) and trends, including:
   * Total number of customers (675), Average Purchase Amount ($60.41), and Average Review Rating (3.72).
   * Revenue and Sales distribution by Category and Age Group.
   * Filters for Subscription Status, Gender, Category, and Shipping Type for customized data exploration.
You can copy and paste this directly into your GitHub README file. Would you like to add anything else to the project documentation?
4. Screenshots
Shoe what the dashboard looks like.
https://github.com/SherivJaswal/Customer-Behavior-Analysis/blob/main/Screenshot%202026-10-08%20003218.png
