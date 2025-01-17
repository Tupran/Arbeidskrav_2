# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:48:30 2025

@author: oag

Oppgave 3

Omregning fra grader til radianer

Det er ikke gitt kriterier for avrunding i oppgaven, men fordi det i
oppgaveteksten er oppgitt kun 4 desimaler på Pi så avrunder jeg til 4 desimaler

"""

import numpy as np

print()
v_grad = float(input('Skriv inn gradtallet: '))

v_rad = v_grad*np.pi/180

print()
print("Vinkel på", v_grad, "er", round(v_rad, 4), "radianer")
print()
