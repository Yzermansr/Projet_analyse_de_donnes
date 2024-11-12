import csv

def half_to_day():
    reader = csv.DictReader(open("national.csv"))
    data = []
    for row in reader:
        data.append((row["HORODATE"], row["REGION"], row["CODE"], row["NB_POINTS_INJECTION"], row["ENERGIE_INJECTEE"], row["GRD"]))
        
    # somme sur les années
    d = {}
    annees = {}
    for h, _, _, _, prod, _ in data:
        try:
            if h[:4] in d.keys():
                d[h[:4]] += int(prod)
                annees[h[:4]] += 1
            else:
                d[h[:4]] = int(prod)
                annees[h[:4]] = 1
                
        except:
            pass
    
    for a, p in d.items():
        print(a, p/10**9)
        
    for a, n in annees.items():
        print(a, n)
    
half_to_day()
    
