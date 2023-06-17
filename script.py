import numpy as np
import matplotlib.pyplot as plt
import os

from skyfield.api import load

data   = load('de421.bsp')
ts     = load.timescale()
t      = ts.utc(2016, 7, 5, 9, 50, 0)

jupiter, earth  = data['Jupiter barycenter'], data['Earth']
jpos, epos      = jupiter.at(t).position.km, earth.at(t).position.km
d_instantaneous = np.sqrt(((jpos - epos)**2).sum())

d_light = earth.at(t).observe(jupiter).distance().km  # where WAS Jupiter 48 minutes ago?

clight = 299792.458  # km/s

print "d_instantaneous / c = ", d_instantaneous/clight
print "d_light / c =         ", d_light/clight

os.system('pause')