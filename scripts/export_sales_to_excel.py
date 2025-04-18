import pandas as pd
sales_report = pd.read_csv('sales_report.csv')
sales_report.to_excel('sales_report.xlsx', index=False)