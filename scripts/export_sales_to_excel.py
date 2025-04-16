import duckdb
import pandas as pd

# Connexion à la base DuckDB persistante
con = duckdb.connect("/data/bottleneck.duckdb")

# Récupérer la table sales_report
df = con.execute("SELECT * FROM sales_report").fetchdf()

# Exporter au format Excel
df.to_excel("/data/sales_report.xlsx", index=False)

print("Fichier Excel exporté avec succès.")