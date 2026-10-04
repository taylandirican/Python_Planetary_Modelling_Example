import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math


class Star:
    def __init__(self, Name, Massxkg, Radiusxm):
        self.Name = Name
        self.Massxkg = Massxkg
        self.Radiusxm = Radiusxm
        self.Inertia = (2 / 5) * Massxkg * (Radiusxm**2)
        self.xLocate = 0
        self.yLocate = 0

    def Gravitational_Acceleration(self, Distancexm):
        G = 6.674e-11

        if Distancexm >= self.Radiusxm:
            return (G * self.Massxkg) / (Distancexm**2)

        elif Distancexm < self.Radiusxm:
            k = 4 / 3 * math.pi * G
            d = self.Massxkg / (4 / 3 * math.pi * (self.Radiusxm**3))
            return k * d * Distancexm


class Planet:
    def __init__(self, Name, Massxkg, Radiusxm, xLocatexm, yLocatexm):
        self.Name = Name
        self.Massxkg = Massxkg
        self.Radiusxm = Radiusxm
        self.Inertia = (2 / 5) * Massxkg * (Radiusxm**2)
        self.xLocatexm = xLocatexm
        self.yLocatexm = yLocatexm

    def Gravitational_Acceleration(self, Distancexm):
        G = 6.674e-11

        if Distancexm >= self.Radiusxm:
            return (G * self.Massxkg) / (Distancexm**2)

        elif Distancexm < self.Radiusxm:
            k = 4 / 3 * math.pi * G
            d = self.Massxkg / (4 / 3 * math.pi * (self.Radiusxm**3))
            return k * d * Distancexm


class Star_System:
    def __init__(self, Name, planet, star):
        self.Name = Name
        self.Planet = planet
        self.Star = star
        self.Distance = math.sqrt(
            ((self.Planet.xLocatexm) ** 2) + ((self.Planet.yLocatexm) ** 2)
        )
        G = 6.674e-11
        v_orb = math.sqrt((G * self.Star.Massxkg) / self.Distance)
        self.Vx = 0
        self.Vy = v_orb * 0.8

    def Gravitational_Forcex(self):
        G = 6.674e-11
        F = (G * self.Star.Massxkg * self.Planet.Massxkg) / (self.Distance) ** 2

        cosx = (self.Planet.xLocatexm) / (self.Distance)

        return -F * cosx

    def Gravitational_Forcey(self):
        G = 6.674e-11
        F = (G * self.Star.Massxkg * self.Planet.Massxkg) / (self.Distance) ** 2

        sinx = (self.Planet.yLocatexm) / (self.Distance)

        return -F * sinx

    def Move(self, time=1000):
        ax = self.Gravitational_Forcex() / self.Planet.Massxkg
        ay = self.Gravitational_Forcey() / self.Planet.Massxkg

        self.Vx = self.Vx + time * ax
        self.Vy = self.Vy + time * ay

        self.Planet.xLocatexm += self.Vx * time
        self.Planet.yLocatexm += self.Vy * time

        self.Distance = math.sqrt(
            (self.Planet.xLocatexm**2) + (self.Planet.yLocatexm**2)
        )


# Calculate

Dünya = Planet("Dünya", 6e24, 6.378e3, 152e9, 0)

Güneş = Star(
    "Güneş",
    2e30,
    696.300e3,
)

Sistem = Star_System("Güneş_Sistemi", Dünya, Güneş)
# Simulation


x_gecmis, y_gecmiş = [], []

fig, ax = plt.subplots(figsize=(12, 12))
ax.set_xlim(-3e11, 3e11)
ax.set_ylim(-3e11, 3e11)
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)

(gunes,) = ax.plot(0, 0, "yo", markersize=50, label="Güneş")
(dünya,) = ax.plot([], [], "bo", markersize=5, label="Dünya")
(yorunge,) = ax.plot([], [], "b--", alpha=0.4, linewidth=1)


def update(frame):
    for i in range(10):
        Sistem.Move()

    x_gecmis.append(Sistem.Planet.xLocatexm)
    y_gecmiş.append(Sistem.Planet.yLocatexm)

    dünya.set_data([Sistem.Planet.xLocatexm], [Sistem.Planet.yLocatexm])
    yorunge.set_data(x_gecmis, y_gecmiş)

    return dünya, yorunge


ani = FuncAnimation(fig, update, frames=240, interval=20, blit=True)

plt.legend()
plt.show()
