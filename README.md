# Friminutt alarm
Dette er et program som spiller av en tilfeldig lydfil når skoletimen min er over

# Hvorfor dette prosjektet?
Jeg valgte å lage dette fordi jeg var intresert i å lære webscraping og jeg ville bli bedre på å skrive python. Det endte opp med at jeg tokk en omvei og brukte en webdriver som simulerer en bruker for å logge seg inn isteden for å webscrape skikkelig, men jeg er fornøyd med hvordan det endte med å bli.

# Hvordan virker den?
Klokken et hver natt logger den seg inn på mitt dashboard på visma for så å hente all koden som ligger bak nettsiden. Så ser den igjenom koden den hentet fra visma til den finner klokkeslettene for hver time og sortere dem etter dag i en 3D liste. Derfra sjekker den hvilken dag det er og henter riktig liste for dagen. så begynner en loop som sjekker klokkeslettet opp imot listen og bestemmer om det er friminutt eller ikke. Dersom det er det spiller den av en av tre lydfiler, ellers venter den et sekund og prøver igjen.
