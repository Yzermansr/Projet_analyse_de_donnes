import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("~/Informatique/Projet_python/Projet_analyse_de_donnes/Données/Importations_et_exportations.csv", delimiter=';', names=["Date", "Filiere", "Frontiere", "Valeur (TWh)"])

data = data[data["Date"] != "Date"]  s
data["Valeur (TWh)"] = pd.to_numeric(data["Valeur (TWh)"].str.replace(',', '.'), errors='coerce')
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
data = data.dropna(subset=['Date'])  

filtrées_data = data[(data["Filiere"].isin(["Importations", "Exportations", "Solde"])) &
                     (data["Frontiere"] == "Toutes les frontières")]

filtrées_data['Year'] = filtrées_data['Date'].dt.year
annual_data = filtrées_data.groupby(['Year', 'Filiere'])['Valeur (TWh)'].sum().unstack()

plt.figure(figsize=(10, 6))
plt.bar(annual_data.index, annual_data['Importations'], color="purple", label="Importations")
plt.bar(annual_data.index, annual_data['Exportations'], color="blue", label="Exportations")
plt.plot(annual_data.index, annual_data['Solde'], color="cyan", marker='o', label="Solde")

plt.xlabel("Année")
plt.ylabel("TWh")
plt.title("Importations et exportations d'électricité en France depuis / vers les pays voisins")
plt.legend(loc="upper right")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()