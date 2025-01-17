# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 19:42:05 2025

@author: oag

Oppgave 4 c (fortsettelse på 4 a og b)

Legge til nye land i "dictionary" og skrive ut "dictionary" til skjermen

Det er ikke lagt føring for hvilket format det skal i dermed presenterer jeg
data i tre forskjellige formater.

https://usn.instructure.com/courses/32917/files/3630404?wrap=1

"""

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

print()
print("Ved registrering av nye land begynn med stor bokstav og resten små")
print("Antall innbyggere oppgis i antall millioner")
print()
land = input('Navnet på landet...............: ')
if land in data:
    print("Landet er allerede registrert")
else:
    hovedstad = input('Navnet på hovedstad............: ')
    innbyggere = float(input('Antall innbyggere i hovedstaden: '))
    data.update({land: [hovedstad, innbyggere]})

    print()
    print()

    antall_land = len(data)
    print("Det er nå registrert", antall_land, "land")
    print()
    print("Det er følgende land (hele dictionary under ett):")
    print()
    print(data)
    print()
    print()
    lands_teller = 0
    print("Det er følgende land (et datasett pr linje):")
    print()
    for key in data:
        print(list(data.items())[lands_teller])
        lands_teller += 1

    print()
    print()
    print("Det er følgende land (tabelloppsett):")
    print()
    print(" %-20s | %-20s | %-16s " % ("Land", "Hovedstad", "Innbygger (mill)"))
    print(64 * "-")
    for land, lands_data in data.items():
        print(" %-20s | %-20s | %-16.3f " % (land, lands_data[0], lands_data[1]))
        lands_teller += 1

print()
