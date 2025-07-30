# Retail Order Data Analysis

## Project Overview

This project focuses on a comprehensive analysis of retail order data. It demonstrates a full data pipeline, from raw data ingestion and cleaning to loading into a PostgreSQL database, and finally, extracting key business insights using SQL queries. The primary goal is to transform raw transactional data into actionable intelligence that can drive strategic business decisions for a retail company.

This repository contains the Python scripts and Jupyter notebooks used for data processing and the SQL queries for analytical reporting.

## Features

* **Data Ingestion:** Reads raw order data from a CSV file.

* **Data Cleaning & Preprocessing:**
    * Handles missing values (`Not Available`, `unknown`).
    * Derives new key performance indicator (KPI) columns: `profit`, `sale_price`, and `discount`.
    * Converts `order_date` to datetime objects for time-series analysis.
    * Drops redundant columns (`list_price`, `cost_price`, `discount_percent`) after calculations.
* **Database Integration:** Connects to a PostgreSQL database using SQLAlchemy to store the cleaned and transformed data.
* **SQL-based Analytics:** Executes advanced SQL queries to answer specific business questions, identifying trends, top performers, and growth metrics.

## Technologies Used

* **Python:** Core programming language for data processing.
* **Pandas:** Powerful library for data manipulation and analysis in Python.
* **SQLAlchemy:** Python SQL toolkit and Object Relational Mapper (ORM) for connecting to and interacting with databases.
* **Psycopg2-binary:** PostgreSQL adapter for Python (used by SQLAlchemy).
* **PostgreSQL:** Robust open-source relational database management system for data storage.
* **Jupyter Notebook:** Interactive computing environment for exploratory data analysis and code development.
* **SQL:** For querying and extracting insights from the PostgreSQL database.

## Dataset

The dataset used for this analysis is the **Retail Orders Dataset** from Kaggle. It contains detailed information about various retail orders, including product details, customer demographics, sales figures, and order dates.

* **Source:** [Retail Orders Dataset on Kaggle](https://www.kaggle.com/datasets/ankitbansal06/retail-orders)
* **File:** `orders.csv` (initially provided within `archive (24).zip`)

