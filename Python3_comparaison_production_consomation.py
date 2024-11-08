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





data2 = pd.read_csv("~/Informatique/Projet_python/Projet_analyse_de_donnes/Données/production-regionale-mensuelle-filiere.csv", sep=";", on_bad_lines="skip")

data2 = data2.drop(['Géo-shape région', 'Géo-point région', 'Code INSEE région', 'Région'], axis=1)
numerique_data2 = data2.select_dtypes(include=["number"]) 
data2 = data2.groupby(['Mois'])[numerique_data2.columns].sum()
print(data)


solde = data2['Production nucléaire (GWh)'] + data2['Production thermique (GWh)'] + data2['Production hydraulique (GWh)'] + data2['Production éolienne (GWh)'] + data2['Production solaire (GWh)'] + data2['Production bioénergies (GWh)']
solde = solde * 1370

data_annuelle2 = data2.groupby('Mois').sum().reset_index()
data_annuelle2['Mois'] = pd.to_datetime(data_annuelle2['Mois'], errors='coerce')




plt.plot(data_annuelle2['Mois'], solde, color="red", marker='o', label="Solde")
plt.plot(data_mois.index, data_mois['Consommation brute électricité (MW) - RTE'], color = "cyan", label = "Consomation", marker = "o")

plt.xlabel("Année")
plt.ylabel("GWh")
plt.title("Production française de 2014 à 2024")
plt.legend(loc="upper right")
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.xticks(rotation=45)

plt.show()