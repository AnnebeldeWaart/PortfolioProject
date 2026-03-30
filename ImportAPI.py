# Benodigde libaries importeren
import requests
import csv
import time

# Api gegevens van adzuna.com
app_id = "478abde6"
api_key = "5f61925208e3cdff7aa6f983bc6df5b7"

# (Lege) Lijst aanmaken om alle vacatures er in op te kunnen slaan
vacatures = []

# loop voor alle pagina's
for page in range(1, 21):
    url = f"https://api.adzuna.com/v1/api/jobs/nl/search/{page}"
    params = {
        "app_id": app_id,
        "app_key": api_key,
        "results_per_page": 50,
        "content-type": "application/json"
    }
    #Api request uitvoeren
    response = requests.get(url, params=params)

    # Checken of het gelukt is zo niet error code:
    if response.status_code != 200:
        print(f"Fout bij pagina {page}: {response.status_code}")
        continue

    data = response.json()

    # Als "results" in de data staan, wordt dat toe gevoegt aan de lege lijst `vacatures = []`
    # Zo niet opvangen met error code
    # `.sleep` om te voorkomen dat de API overbelast raakt
    if "results" in data:
        vacatures.extend(data["results"])
    else:
        print(f"Geen 'results' gevonden op pagina {page}")
    time.sleep(1)

# De Vacatures worden opgeslagen in een csv bestand
with open("vacatures.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    # Structuur van het Csv bestand bepalen met headers
    writer.writerow(["title", "company", "location", "category", "salary_min", "salary_max", "created"])
    
    # Elke vacature als een aparte rij opslaan
    for vacature in vacatures:
        writer.writerow([
            vacature.get("title"),
            vacature.get("company", {}).get("display_name"),
            vacature.get("location", {}).get("display_name"),
            vacature.get("category", {}).get("label"),
            vacature.get("salary_min"),
            vacature.get("salary_max"),
            vacature.get("created")
        ])
# Het Aantal opgeslagen vacatures printen
print(f"{len(vacatures)} vacatures opgeslagen in vacatures.csv") 