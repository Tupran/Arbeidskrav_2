# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:29:03 2025

@author: oag

Oppgave 2

Pizza beregning

Programmet skal så regne ut hvor mange pizzaer må skal handles inn

Velger også å legge til test på antall pizzaer og elever for gramatikken

"""

import math

antall_elever = int(input('Skriv inn antall elever: '))

antall_pizzaer = math.ceil(antall_elever/4)

print()
if antall_pizzaer == 1:
    if antall_elever == 1:
        print("Med", antall_elever, "elev trengs det", antall_pizzaer, "pizza til festen")
    else:
        print("Med", antall_elever, "elever trengs det", antall_pizzaer, "pizza til festen")
else:
    print("Med", antall_elever, "elever trengs det", antall_pizzaer, "pizzaer til festen")
print()
