import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates  


data = pd.read_csv("~/Informatique/Projet_python/Projet_analyse_de_donnes/Données/production-regionale-mensuelle-filiere.csv", sep=";", on_bad_lines="skip")

data = data.drop(['Géo-shape région', 'Géo-point région', 'Code INSEE région', 'Région'], axis=1)



numerique_data = data.select_dtypes(include=["number"]) 
data = data.groupby(['Mois'])[numerique_data.columns].sum()

solde = data['Production nucléaire (GWh)'] + data['Production thermique (GWh)'] + data['Production hydraulique (GWh)'] + data['Production éolienne (GWh)'] + data['Production solaire (GWh)'] + data['Production bioénergies (GWh)']

data_annuelle = data.groupby('Mois').sum().reset_index()
data_annuelle['Mois'] = pd.to_datetime(data_annuelle['Mois'], errors='coerce')

fig, ax = plt.subplots()
ax.plot(data_annuelle['Mois'], solde, color="cyan", marker='o', label="Solde")


ax.xaxis.set_major_locator(mdates.YearLocator()) 
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  


plt.xlabel("Année")
plt.ylabel("GWh")
plt.title("Production française de 2014 à 2024")
plt.legend(loc="upper right")
plt.grid(axis='y', linestyle='--', alpha=0.7)


plt.xticks(rotation=45)

plt.show()
