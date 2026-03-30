# Vacatures API Scraper en Salaris Outlier Analyse

## Over dit project

Dit project bestaat uit twee documenten die samen de vacaturedata op halen uit de Adzuna API. Dit sla ik dan op in een CSV-bestand, daarna maak ik het helemaal schoon en vervolgens salaris-outliers te detecteren met voor mij nieuwe machine-learning technieken.

Het project is handig/boedoelt voor:

- data-analyse
- arbeidsmarktanalyse
- datacleaning
- outlier-detectie
- machine learning

## Wat doet het project?

Het project heeft twee orderdelen:

1. `scraper.py`
   - haalt vacatures op uit de Adzuna Jobs API
   - slaat de data op in `vacatures.csv`

2. `analyse.py`
   - leest `vacatures.csv` in
   - maakt de data schoon
   - vult ontbrekende salariswaarden aan
   - maakt extra features
   - detecteert outliers in salarissen
   - maakt een test visualisatie van de resultaten

## Benodigdheden

Voor dit project heb je Python nodig, samen met de volgende libraries:

- requests
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

Installatie
1. Python installeren

Zorg dat Python op je computer staat geïnstalleerd.

2. Project openen

Open de projectmap in VS Code of een andere editor.

3. Libraries installeren

Installeer de libraries met:
Kopier het volgende in de terminal:

`pip install requests pandas numpy matplotlib seaborn scikit-learn`

**Mogelijke problemen:**
`Geen module gevonden`

Als je een fout krijgt zoals ModuleNotFoundError, installeer dan opnieuw de dependencies.

4. API-gegevens invullen

In scraper.py staan deze regels bovenaan:

Je moet een app id en een api key hebben om de api te mogen gebruiken:

`app_id = "478abde6"`

`api_key = "5f61925208e3cdff7aa6f983bc6df5b7"`

**Mogelijke problemen:** CSV-bestand bestaat niet

Als analyse.py zegt dat vacatures.csv ontbreekt, dan moet je eerst scraper.py draaien.

API geeft fouten terug

Controleer dan:

- of app_id correct is
- of api_key correct is
- of de API nog werkt
- of je niet te snel te veel requests verstuurt

## Gebruik:

Stap 1: Vacatures ophalen:

Voer eerst het scraper-script uit in de terminal:

`python scraper.py`

Dit script:

- maakt een lijst aan voor vacatures
- doorloopt pagina 1 tot en met 20
- haalt per pagina maximaal 50 vacatures op
- controleert of de API-call succesvol is
- voegt de resultaten toe aan de lijst
- slaat alles op in vacatures.csv

Aan het einde zie je iets zoals:

`1000 vacatures opgeslagen in vacatures.csv`
ls er een fout optreedt op een pagina, wordt dit in de terminal gemeld.

---

## Stap 2: Data analyseren en opschonen

Voer het analyse-script uit:

Door op run te klikken boven aan vscode

Dit script leest vacatures.csv in en voert de volgende stappen uit:

### 1. Data inladen

De CSV wordt geladen met pandas:

`df = pd.read_csv("vacatures.csv")`

2. Categorie opschonen

Sommige categorieën zijn niet bruikbaar, bijvoorbeeld:

unknown
vacatures ander of algemeen

Deze worden vervangen door de functietitel.

Daarna wordt de titel opgeschoond door delen van de tekst te verwijderen na tekens zoals:

- |
- /
- (
- \

De categorie wordt daarna omgezet naar een nette schrijfwijze met hoofdletters.

---

## 3. Salaris opschonen

De kolommen salary_min en salary_max worden omgezet naar numerieke waarden. Ongeldige waarden worden NaN.

Daarna wordt per categorie de mediaan berekend en gebruikt om ontbrekende waarden in te vullen.

---

## 4. Nieuwe features maken

Het script maakt extra kolommen aan:

`salary_mean`: Het gemiddelde van minimum- en maximumsalaris
`salary_range`: Het verschil tussen maximum- en minimumsalaris
`salary_log`: Log-transformatie van het gemiddelde salaris

Deze extra kolommen helpen bij de outlier-detectie.

---

## 5. Contamination bepalen per categorie

Voor elke categorie wordt bepaald hoeveel records waarschijnlijk outliers zijn. Dit gebeurt op basis van de IQR-methode.

De uitkomst wordt begrensd:

- minimaal 0.045
- maximaal 0.25

Zo blijft het model niet te streng en niet te soepel.

---

## 6. Outlier-detectie

Het script gebruikt een combinatie van twee methoden:

### IQR-methode
Er worden kwartielen berekend:

Q1 Q3 IQR = Q3 - Q1

Waarden buiten de grenzen worden als verdacht gezien.

### Isolation Forest

Daarnaast wordt per categorie een Isolation Forest-model gebruikt met:

`salary_log` en `salary_range`

Een observatie wordt alleen als outlier gemarkeerd als:

Isolation Forest voorspelt -1
en de waarde ook buiten de IQR-grenzen valt

---

## 7. Resultaten tonen

Het script print:

- Het aantal outliers per categorie
- De oorspronkelijke datasetgrootte
- De opgeschoonde datasetgrootte

---

## 8. Visualisatie

Er wordt een scatterplot gemaakt voor de categorie: **Bouwkunde Vacatures**

In deze grafiek geldt:

- Blauw = normale observaties
- Rood = outliers

De x-as toont de observatie-index en de y-as toont salary_mean.

---

## Outputbestanden

Na het draaien van de scripts kun je deze bestanden hebben:

- vacatures.csv
- De ruwe vacaturedata van de API
- Eventueel een opgeschoonde dataset. (Als je dit zelf uitbreidt in je script)
- Eventueel een bestand met outliers. (Als je dit zelf toevoegt aan je analyse)