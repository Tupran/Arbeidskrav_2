# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 09:54:11 2025

@author: oag

Kode som plotter funksjonen 𝑓(𝑥) = −𝑥^2 − 5, for x på intervallet [-10,10].

"""

import numpy as np
import matplotlib.pyplot as plt

x_tabell = np.linspace(-10, 10, 200)

plt.title('f(x) = -x^2 - 5')
plt.plot(x_tabell, -x_tabell ** 2 - 5)

plt.show()
