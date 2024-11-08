import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("~/Informatique/Projet_python/Projet_analyse_de_donnes/Données/Consomation_quotidienne.csv", sep=";", on_bad_lines="skip")

data = data.drop(['Consommation brute gaz (MW PCS 0°C) - GRTgaz', 'Statut - GRTgaz',
       'Consommation brute gaz (MW PCS 0°C) - Teréga', 'Statut - Teréga',
       'Consommation brute gaz totale (MW PCS 0°C)','Statut - RTE',
       'Consommation brute totale (MW)','Heure','Date - Heure'], axis = 1)

data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
data = data.groupby(['Date']).sum()
data_mois = data.resample('M').sum()


plt.plot(data_mois.index, data_mois['Consommation brute électricité (MW) - RTE'], color = "cyan", label = "Consomation", marker = "o")

plt.xlabel("Année")
plt.ylabel("GWh")
plt.title("Production française de 2014 à 2024")
plt.legend(loc="upper right")
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.xticks(rotation=45)

plt.show()



