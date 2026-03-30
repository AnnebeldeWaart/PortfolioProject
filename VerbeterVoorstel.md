# Verbetervoorstel:

## Verbetervoorstellen op basis van testresultaten

**1. Toepassen van een AI-model voor outlier-detectie**  
Op basis van de testresultaten van de salarisdata is gebleken dat er veel afwijkende waarden (outliers) en inconsistente data aanwezig zijn. Dit heeft een negatieve invloed op de betrouwbaarheid van analyses.

Als verbetering stel ik voor om een AI-model te implementeren, zoals een Isolation Forest, om automatisch outliers in de salarisdata te detecteren en te filteren. Dit model kan leren welke waarden afwijken van de normale verdeling en deze markeren of verwijderen.

Daarnaast kan de IQR-methode (Interquartile Range) gebruikt worden als ondersteuning om per categorie een eerste inschatting te maken van de spreiding en mogelijke outliers. Deze informatie kan vervolgens gebruikt worden om het AI-model beter af te stellen, bijvoorbeeld door de contamination parameter dynamisch te bepalen.

Door deze combinatie van statistische en machine learning technieken kan de data automatisch opgeschoond worden, zelfs wanneer deze via een live API binnenkomt.

**2. Betere error handling implementeren**  
Tijdens het testen kwamen verschillende errors voor, bijvoorbeeld bij het inladen van data.  
Een verbetering is om deze errors beter op te vangen, zodat het systeem stabieler wordt en minder snel vastloopt.

**3. Toevoegen van visualisaties**  
Tijdens het testen was het lastig om snel inzicht te krijgen in de data.  
Door visualisaties zoals boxplots toe te voegen, kunnen outliers sneller en duidelijker worden geanalyseerd.

---

## Verbetervoorstellen op basis van oplevering

**4. Omzetten naar herbruikbare code**  
De huidige oplossing zit in een notebook en is nog niet volledig herbruikbaar.  
Een verbetering is om de code om te zetten naar functies of een pipeline, zodat deze makkelijker opnieuw gebruikt kan worden.

Een verbetering is om de code om te zetten naar herbruikbare functies of een pipeline. Dit maakt de oplossing beter inzetbaar binnen de opdracht en sluit aan bij de user story waarin betrouwbare en herbruikbare data-analyse centraal staat.  

Dit verbetert de functionaliteit en het gebruik van de software.

**5. Integratie in een data pipeline**  
De testresultaten tonen aan dat data opschoning een essentieel onderdeel is van het proces. Momenteel gebeurt dit losstaand.

De oplossing werkt nu los van de rest van het systeem.  
In de toekomst kan dit geïntegreerd worden in een automatische data pipeline, zodat data direct opgeschoond wordt bij het inladen van de API.

Dit sluit aan bij de opdracht om een werkende en efficiënte oplossing te ontwikkelen en zorgt ervoor dat gebruikers altijd met schone data werken.

**6. Dagelijks verversen van data via de API**  
Tijdens de test is gewerkt met statische data, terwijl de API live data levert.  

Op dit moment wordt de data handmatig ingeladen.  
Een verbetering is om de API dagelijks automatisch te laten draaien, zodat de dataset altijd up-to-date blijft en analyses gebaseerd zijn op actuele data.

Dit verhoogt de praktische bruikbaarheid van de applicatie.

---

## Verbetervoorstellen op basis van eigen reflectie

**7. Werken met een duidelijk stappenplan**  
Tijdens het proces heb ik gemerkt dat ik zonder vast stappenplan werkte, waardoor ik soms stappen moest herhalen.

Ik gemerkt dat ik soms zonder duidelijke structuur begon te werken.  
In een volgend project wil ik vooraf een stappenplan maken, zodat ik stapsgewijs kan werken en beter overzicht houd over het proces.

Dit heeft direct betrekking op mijn rol in het project, waarin ik verantwoordelijk was voor het analyseren en opschonen van data.

**8. Meer structuur in het ontwikkelproces**  
Ik merkte dat ik soms meerdere dingen tegelijk probeerde op te lossen, wat het proces onoverzichtelijk maakte.  
Een verbetering is om per stap één probleem tegelijk aan te pakken en deze eerst volledig af te ronden voordat ik verder ga.

In de toekomst wil ik per stap werken en eerst één probleem volledig oplossen voordat ik verder ga. Dit zorgt voor een duidelijker ontwikkelproces en betere controle over de resultaten.

**9. Gebruik van comments in code**  
Tijdens het coderen heb ik niet altijd voldoende comments toegevoegd.  
Het is duidelijker om tijdens het programmeren direct comments schrijven, zodat later duidelijk is wat de code doet en waarom bepaalde keuzes zijn gemaakt.

Een verbetering is om tijdens het programmeren direct comments toe te voegen en keuzes te documenteren. Dit maakt mijn werk beter navolgbaar en professioneler.  

Dit sluit aan bij mijn rol als ontwikkelaar, waarbij duidelijke communicatie en overdraagbaarheid belangrijk zijn.