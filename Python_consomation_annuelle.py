import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("~/Informatique/Projet_python/Projet_analyse_de_donnes/Données/Consomation_annuelle.csv", sep=';')
data = data.drop(['Consommation brute gaz (GWh PCS 0°C) - GRTgaz','Statut - GRTgaz',
                  'Consommation brute gaz (GWh PCS 0°C) - Teréga','Statut - Teréga',
                  'Consommation brute gaz totale (GWh PCS 0°C)','Consommation brute électricité (GWh) - RTE',
                  'Statut - RTE','Consommation brute totale (GWh)'], axis=1)
data['Année'] = pd.to_datetime(data['Année'], format='%Y', errors='coerce')
data = data.dropna(subset=['Année'])
data = data[data['Année'] >= '2014-01-01']
data.set_index('Année', inplace=True)

data2 = pd.read_csv("~/Informatique/Projet_python/Projet_analyse_de_donnes/Données/production-regionale-mensuelle-filiere.csv", sep=";", on_bad_lines="skip")
data2 = data2.drop(['Géo-shape région', 'Géo-point région', 'Code INSEE région', 'Région'], axis=1)
numerique_data2 = data2.select_dtypes(include=["number"])
data2 = data2.groupby(['Mois'])[numerique_data2.columns].sum()
solde = data2['Production nucléaire (GWh)'] + data2['Production thermique (GWh)'] + data2['Production hydraulique (GWh)'] + data2['Production éolienne (GWh)'] + data2['Production solaire (GWh)'] + data2['Production bioénergies (GWh)']
data_annuelle2 = data2.groupby('Mois').sum().reset_index()
data_annuelle2['Mois'] = pd.to_datetime(data_annuelle2['Mois'], errors='coerce')
data_annuelle2.set_index('Mois', inplace=True)
data_monthly = data_annuelle2.resample('Y').sum()
solde.index = pd.to_datetime(data2.index, errors='coerce')
solde_annuelle = solde.resample('Y').sum()



fig, ax = plt.subplots(figsize=(10, 6))
Années = data.index.year 
ax.bar(data_monthly.index.year, solde_annuelle, color="red", width=0.4, label="Solde", align='center')
ax.bar(Années, data['Consommation corrigée électricité (GWh) - RTE'], color="cyan", width=0.4, label="Consommation", align='edge')


ax.set_xlabel("Année")
ax.set_ylabel("GWh")
ax.set_title("Production et Consommation française de 2014 à 2024")
ax.legend(loc="upper right")
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()