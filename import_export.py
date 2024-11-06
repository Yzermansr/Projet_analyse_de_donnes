import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
file_path = '~/Informatique/Projet_python/Projet_analyse-_de_donn-es/Données/imports-exports-commerciaux.csv'
data = pd.read_csv(file_path, delimiter=';')

# Convertir la colonne 'Date' pour permettre le groupement par année
data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

# Grouper par année et calculer les totaux annuels pour les colonnes numériques
annual_data = data.groupby(data['Date'].dt.year).sum(numeric_only=True)

# Calculer le solde entre exportations et importations
annual_data['Solde (MWh)'] = annual_data['Export France (MWh)'] + annual_data['Import France (MWh)']

# Conversion des valeurs en TWh pour correspondre au graphique de référence
annual_data['Import France (TWh)'] = annual_data['Import France (MWh)'] / 1_000_000
annual_data['Export France (TWh)'] = annual_data['Export France (MWh)'] / 1_000_000
annual_data['Solde (TWh)'] = annual_data['Solde (MWh)'] / 1_000_000

# Créer le graphique
plt.figure(figsize=(14, 7))

# Barres empilées pour les importations et exportations
plt.bar(annual_data.index, annual_data['Import France (TWh)'], label='Importations', color='purple')
plt.bar(annual_data.index, annual_data['Export France (TWh)'], label='Exportations', color='blue', alpha=0.7, bottom=annual_data['Import France (TWh)'])

# Tracer la courbe du solde
plt.plot(annual_data.index, annual_data['Solde (TWh)'], color='cyan', marker='o', label='Solde')

# Configuration des axes et du graphique
plt.xlabel('Année')
plt.ylabel('TWh')
plt.title("Importations et exportations d'électricité en France depuis / vers les pays voisins")
plt.legend()
plt.grid()

# Afficher le graphique
plt.tight_layout()
plt.show()