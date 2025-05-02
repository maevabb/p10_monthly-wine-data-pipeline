
# Data Pipeline Orchestration – BottleNeck

✨ Author: Maëva Beauvillain 📅 Start Date: April 2025 📅  Last Updated: May 2, 2025

## Context

BottleNeck is a renowned wine merchant seeking to automate its monthly sales analysis to support product managers in targeting their marketing strategies more effectively. This project focuses on industrializing a previously manual analysis process.

## Objectives

- Clean and reconcile datasets from two systems (ERP & CMS)
- Calculate total and per-product revenue
- Identify premium wines using the **z-score** method
- Generate `.xlsx` and `.csv` reports
- Automate execution and export results to AWS S3
- Integrate quality checks at each key stage

## Pipeline Architecture

This pipeline is orchestrated using **Kestra** and includes:
- SQL scripts executed via **DuckDB**
- Python scripts for additional processing
- Test tasks embedded within the pipeline
- A scheduled run on the **15th of each month at 9:00 AM**

## Project Structure

```
.
├── .env
├── docker-compose.yml
├── pyproject.toml
├── poetry.lock
├── Pipeline d'orchestration des flux.pptx  # Final presentation
├── data/
│   ├── Fichier_erp.xlsx
│   ├── fichier_liaison.xlsx
│   ├── Fichier_web.xlsx
│   ├── *.csv (intermediate & output files)
│   └── bottleneck.duckdb
├── _flows/
│   └── monthly-wine-data-pipeline.yml  # Main Kestra flow
└── scripts/
    ├── xlsx_to_csv.py
```

## Pipeline Stages

### 1. Extraction & Conversion
- Download Excel files (ERP, Liaison, Web)
- Convert them to `.csv` using `xlsx_to_csv.py`

### 2. Cleaning & Testing
- Remove rows with missing values (`product_id`, `sku`)
- Remove duplicates using DuckDB
- Run tests for nulls and duplicates

### 3. Data Reconciliation
- Join the 3 datasets using `product_id` and `sku`
- Run a consistency check on the joins

### 4. Revenue Calculation
- Compute total and per-product revenue
- Generate the final `sales_report.xlsx`
- Run validation tests on calculated values

### 5. Wine Classification
- Apply z-score to price using `scipy.stats.zscore`
- Identify **premium wines** (z-score > 2)
- Export `premium_wines.csv` and `ordinary_wines.csv`
- Run classification integrity tests

### 6. Export
- Upload all result files to **AWS S3**

## Built-in Tests

Automated validation tasks are included throughout the pipeline:

| Stage                  | Tests performed                     |
|------------------------|-------------------------------------|
| Cleaning               | Missing values, duplicates          |
| Join                   | Record consistency                  |
| Revenue calculation    | Price × Quantity = Total check      |
| Z-score classification | Threshold validation (z > 2)        |

## Scheduling

The workflow runs on a **monthly schedule** using a cron expression:  
```
0 9 15 * *  → Every 15th of the month at 09:00 AM
```

## Dependencies

- **Kestra** for orchestration
- **DuckDB** for SQL queries
- **Python 3.10** with `pandas`, `scipy`, `openpyxl`
- **AWS S3** for cloud storage

## Local Execution (optional)

> This pipeline is designed for a cloud-based orchestration system.  
To run locally, make sure you have:
- Docker & Docker Compose
- Kestra installed (via container)
- Python and Poetry

## Outputs

- `sales_report.xlsx` → Wine revenues by product
- `premium_wines.csv` → Premium wines only
- `ordinary_wines.csv` → Remaining wines
- All files uploaded to AWS S3: `sales_reports/`, `wines/`

---

Project developed as part of the **Data Engineer** training program by OpenClassrooms.
