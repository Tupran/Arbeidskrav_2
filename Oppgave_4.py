# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:59:47 2025

@author: oag

Oppgave 4 a og b

Oppslag i "dictionary"

"""

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

print()
land = input('Velg et land (Begynn med stor bokstav og resten små): ')


print()
if land in data:
    lands_data = data[land]
    hovedstad = lands_data[0]
    innbyggere = lands_data[1]
    print(hovedstad, "er hovedstaden i", land, "og det er", innbyggere, "mill. innbyggere i", hovedstad)
else:
    print("Landet er ikke registret - Sjekk eventuelt for skrivefeil")
print()
