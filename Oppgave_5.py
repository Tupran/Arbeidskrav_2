# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 09:14:36 2025

@author: oag

Programmet har en funksjon som tar a og b som inn-argumenter og som så
regner ut arealet og «ytre» omkrets til en figur satt sammen av en rettvinklet
trekant og en halvsirkel. Halvsirkelen har a som diameter.

a og b er katetene i trekanten

"""

import math as mp


def data_inn():
    print()
    a = float(input("Skriv inn verdien for a: "))
    b = float(input("Skriv inn verdien for b: "))
    return (a, b)


data_a_b = data_inn()

katet1 = data_a_b[0]
katet2 = data_a_b[1]
hypotenus = mp.hypot(katet1, katet2)

areal = mp.pi*mp.sqrt(katet1/2)/2 + katet1*katet2/2
omkrets = mp.pi*katet1/2 + katet2 + hypotenus

print()
print("Arealet av figuren er..:", areal)
print("Omkretsen av figuren er:", omkrets)
print()
