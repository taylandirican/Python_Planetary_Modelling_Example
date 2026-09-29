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
    def __init__(self, Name, Massxkg, Radiusxm, xLocatexm, ylocatexm):
        self.Name = Name
        self.Massxkg = Massxkg
        self.Radiusxm = Radiusxm
        self.Inertia = (2 / 5) * Massxkg * (Radiusxm**2)
        self.xLocate = xLocatexm
        self.yLocate = ylocatexm

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
            ((self.Planet.xLocate) ** 2) + ((self.Planet.yLocate) ** 2)
        )

    def Gravitational_Forcex(self):
        G = 6.674e-11
        F = (G * self.Star.Massxkg * self.Planet.Massxkg) / (
            self.Distance + self.Planet.Radiusxm + self.Star.Radiusxm
        )

        sinx = (self.Planet.xLocatexm) / math.sqrt((self.Planet.xLocatexm) ** 2) + (
            (self.Planet.yLocatexm) ** 2
        )

        return F * sinx

    def Gravitational_Forcey(self):
        G = 6.674e-11
        F = (G * self.Star.Massxkg * self.Planet.Massxkg) / (
            self.Distance + self.Planet.Radiusxm + self.Star.Radiusxm
        )

        siny = (self.Planet.yLocatexm) / math.sqrt((self.Planet.xLocatexm) ** 2) + (
            (self.Planet.yLocatexm) ** 2
        )

        return F * siny

    def Vx(self):
        G = 6.674e-11
        v = math.sqrt(
            (G * self.Star.Massxkg) / self.Distance
            + self.Planet.Radiusxm
            + self.Star.Radiusxm
        )

        sinx = (self.Planet.xLocatexm) / math.sqrt((self.Planet.xLocatexm) ** 2) + (
            (self.Planet.yLocatexm) ** 2
        )

        return v * sinx

    def Vy(self):
        G = 6.674e-11
        v = math.sqrt(
            (G * self.Star.Massxkg) / self.Distance
            + self.Planet.Radiusxm
            + self.Star.Radiusxm
        )

        siny = (self.Planet.yLocatexm) / math.sqrt((self.Planet.xLocatexm) ** 2) + (
            (self.Planet.yLocatexm) ** 2
        )

        return v * siny

    def Wx(self):
        return self.Vx() / (self.Distance + self.Planet.Radiusxm + self.Star.Radiusxm)

    def Wy(self):
        return self.Vy() / (self.Distance + self.Planet.Radiusxm + self.Star.Radiusxm)

    def Move(self, timexday):
        time = timexday * 24 * 60 * 60
        i = 0
        while i <= time:
            x_gecmis = time * self.Vx
            y_gecmis = time * self.Vy
            self.Vx = time * self.Gravitational_Forcex / self.Planet.Massxkg
            self.Vy = time * self.Gravitational_Forcey / self.Planet.Massxkg
            i = i + (24 * 60 * 60)


# Simulation


fig, ax = plt.subplots()
ax.set_xlim(-2e11, 2e11)
ax.set_ylim(-2e11, 2e11)

gunes = ax.plot(0, 0, "yo", markersize=10, label="Güneş")
dünya = ax.plot([], [], "bo", markersize=6, label="Dünya")
gunes = ax.plot([], [], "b--", alpha=0.5)

x_gecmis, y_gecmiş = [], []


# Calculate

Dünya = Planet("Dünya", 6e24, 6.378e3, 152e9, 0)

Güneş = Star(
    "Güneş",
    2e30,
    696.300e3,
)

Sistem = Star_System("Güneş_Sistemi", Dünya, Güneş)

print(Sistem.Gravitational_Force())
print(Sistem.V())
print(Sistem.W())
print(Sistem.Angular_Momentum())
print(Dünya.Gravitational_Acceleration(7000e3))
