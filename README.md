# Friminutt alarm
Dette er et program som spiller av en tilfeldig lydfil når skoletimen min er over 

# Hvorfor dette prosjektet?
Jeg valgte å lage dette fordi jeg var interessert i å lære webscraping og jeg ville bli bedre på å skrive Python. Det endte opp med at jeg tokk en omvei og brukte en webdriver som simulerer en bruker for å logge seg inn istedenfor å webscrape skikkelig, men jeg er fornøyd med hvordan det endte med å bli. 

# Hvordan virker den?
Klokken 01:00 hver natt logger programmet seg inn på mitt Dashboard på Visma for så å hente all koden som ligger bak nettsiden. Så ser den igjennom koden den hentet fra Visma til den finner klokkeslettene for hver time og sortere dem etter dag i en 3D-liste. Derfra sjekker den hvilken dag det er og henter riktig liste for dagen. Så begynner en loop som sjekker klokkeslettet opp imot listen og bestemmer om det er friminutt eller ikke. Dersom det er det spiller den av en av tre lydfiler, ellers venter den et sekund og prøver igjen. Denne loopen fortsetter til klokken 01:00 neste dag. 
