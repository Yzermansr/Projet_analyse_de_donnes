import csv

def half_hour_to_day():
    # ouvrir la copie
    reader = csv.DictReader(open("production-demi-horaire-agregee-par-region.csv"))
    data = []
    for row in reader:
        if row["REGION"] == "National":
            data.append((row["HORODATE"], row["REGION"], row["CODE"], row["NB_POINTS_INJECTION"], row["ENERGIE_INJECTEE"], row["GRD"]))
    
    to_nat_file(data)
    
def to_nat_file(data):
    with open("national.csv", mode="w", newline="") as file:
        
        writer = csv.writer(file)
        writer.writerow(["HORODATE","REGION","CODE","NB_POINTS_INJECTION","ENERGIE_INJECTEE","GRD"])
        writer.writerows(data)  # Écrit plusieurs lignes
    
half_hour_to_day()
        
    
