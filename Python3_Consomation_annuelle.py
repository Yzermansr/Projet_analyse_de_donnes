import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("~/Informatique/Projet_python/Projet_analyse_de_donnes/Données/Consomation_annuelle.csv", sep=';')
data = data.drop(['Consommation brute gaz (GWh PCS 0°C) - GRTgaz','Statut - GRTgaz',
                  'Consommation brute gaz (GWh PCS 0°C) - Teréga','Statut - Teréga',
                  'Consommation brute gaz totale (GWh PCS 0°C)','Consommation brute électricité (GWh) - RTE',
                  'Statut - RTE','Consommation brute totale (GWh)'], axis=1)
data['Année'] = pd.to_datetime(data['Année'], format='%Y', errors='coerce')
data = data.dropna(subset=['Année'])
data.set_index('Année', inplace=True)

print(data)
Fig, ax = plt.subplots(figsize=(10, 6))
Années = data.index.year 

ax.plot(Années, data['Consommation corrigée électricité (GWh) - RTE'],"ob")


ax.set_xlabel("Année")
ax.set_ylabel("GWh")
ax.set_title("Production et Consommation française de 2014 à 2024")
ax.legend(loc="upper right")
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()