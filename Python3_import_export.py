import pandas as pd
import matplotlib.pyplot as plt

# Charger les données depuis le fichier CSV
data = pd.read_csv("~/Informatique/Projet_python/Projet_analyse_de_donnes/Données/Importations_et_exportations.csv", delimiter=';', names=["Date", "Filiere", "Frontiere", "Valeur (TWh)"])

# Nettoyer et transformer les données
data = data[data["Date"] != "Date"]  # Supprimer les lignes d'en-tête répétées
data["Valeur (TWh)"] = pd.to_numeric(data["Valeur (TWh)"].str.replace(',', '.'), errors='coerce')
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
data = data.dropna(subset=['Date'])  # Supprimer les dates non valides

# Filtrer pour "Importations", "Exportations" et "Solde" pour toutes les frontières
filtered_data = data[(data["Filiere"].isin(["Importations", "Exportations", "Solde"])) &
                     (data["Frontiere"] == "Toutes les frontières")]

# Aggréger les données par année
filtered_data['Year'] = filtered_data['Date'].dt.year
annual_data = filtered_data.groupby(['Year', 'Filiere'])['Valeur (TWh)'].sum().unstack()



# Créer le graphique
plt.figure(figsize=(10, 6))
plt.bar(annual_data.index, annual_data['Importations'], color="purple", label="Importations")
plt.bar(annual_data.index, annual_data['Exportations'], color="blue", label="Exportations")
plt.plot(annual_data.index, annual_data['Solde'], color="cyan", marker='o', label="Solde")

# Ajouter les détails
plt.xlabel("Année")
plt.ylabel("TWh")
plt.title("Importations et exportations d'électricité en France depuis / vers les pays voisins")
plt.legend(loc="upper right")
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()