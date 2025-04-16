import pandas as pd

erp = pd.read_excel("data/Fichier_erp.xlsx")
web = pd.read_excel("data/Fichier_web.xlsx")
liaison = pd.read_excel("data/fichier_liaison.xlsx")

erp.to_csv("erp.csv", index=False)
web.to_csv("web.csv", index=False)
liaison.to_csv("liaison.csv", index=False)
