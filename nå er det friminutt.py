# Denne filen sjekker klokkeslettet og spiller lyden

import random
import vismaloggin
from datetime import datetime
from time import sleep
from playsound import playsound


def snakk():
    stemme = random.randint(1, 3)
    if stemme == 1:
        playsound(r"C:\Users\Martin\PycharmProjects\Friminutt-alarm\lydfiler\Friminutt 1.mp3")
    elif stemme == 2:
        playsound(r"C:\Users\Martin\PycharmProjects\Friminutt-alarm\lydfiler\Friminutt 2.mp3")
    elif stemme == 3:
        playsound(r"C:\Users\Martin\PycharmProjects\Friminutt-alarm\lydfiler\Friminutt 3.mp3")
    print("Friminutt!!!!")


tid = [[0]]
tid = list(vismaloggin.loggin())
print(tid)
while tid == [[0]] or tid == [[]]:
    print("Webscraping failed")
    tid = list(vismaloggin.loggin())
    print(tid)


while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    current_time = current_time.replace(":", "")
    if str(current_time) in str(tid):
        snakk()
        sleep(60)
    else:
        if random.randint(1, 2) == 1:
            print("ikke friminutt enda")
        else:
            print("nei ikke enda, sitt ned og jobb")
        print(now.strftime("%H:%M:%S"))
    if current_time == "0100":
        tid = vismaloggin.loggin()
        while tid == [[0]] or tid == [[]] :
            tid = list(vismaloggin.loggin())
            print("Webscraping failed")
            print(tid)
        sleep(60)
        # venter et minutt for å ungå å spille en lydfil hvert sekund ettersom programmet ikke bryr seg om sekunder.  
    sleep(1)
