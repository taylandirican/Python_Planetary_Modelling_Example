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

    def Gravitational_Forcex(self):
        G = 6.674e-11
        F = (G * self.Star.Massxkg * self.Planet.Massxkg) / (
            self.Distance + self.Planet.Radiusxm + self.Star.Radiusxm
        )

        sinx = (self.Planet.xLocatexm) / math.sqrt((self.Planet.xLocatexm) ** 2) + (
            (self.Planet.yLocatexm) ** 2
        )

        if self.Planet.xLocatexm > 0 and self.Planet.yLocatexm > 0:
            return -F * sinx
        if self.Planet.xLocatexm < 0 and self.Planet.yLocatexm > 0:
            return +F * sinx
        if self.Planet.xLocatexm < 0 and self.Planet.yLocatexm < 0:
            return +F * sinx
        if self.Planet.xLocatexm > 0 and self.Planet.yLocatexm < 0:
            return -F * sinx

    def Gravitational_Forcey(self):
        G = 6.674e-11
        F = (G * self.Star.Massxkg * self.Planet.Massxkg) / (
            self.Distance + self.Planet.Radiusxm + self.Star.Radiusxm
        )

        siny = (self.Planet.yLocatexm) / math.sqrt((self.Planet.xLocatexm) ** 2) + (
            (self.Planet.yLocatexm) ** 2
        )

        if self.Planet.xLocatexm > 0 and self.Planet.yLocatexm > 0:
            return -F * siny
        if self.Planet.xLocatexm < 0 and self.Planet.yLocatexm > 0:
            return -F * siny
        if self.Planet.xLocatexm < 0 and self.Planet.yLocatexm < 0:
            return +F * siny
        if self.Planet.xLocatexm > 0 and self.Planet.yLocatexm < 0:
            return +F * siny

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

        if self.Planet.xLocatexm > 0 and self.Planet.yLocatexm > 0:
            return -v * sinx
        if self.Planet.xLocatexm < 0 and self.Planet.yLocatexm > 0:
            return -v * sinx
        if self.Planet.xLocatexm < 0 and self.Planet.yLocatexm < 0:
            return +v * sinx
        if self.Planet.xLocatexm > 0 and self.Planet.yLocatexm < 0:
            return +v * sinx

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

        if self.Planet.xLocatexm > 0 and self.Planet.yLocatexm > 0:
            return +v * siny
        if self.Planet.xLocatexm < 0 and self.Planet.yLocatexm > 0:
            return -v * siny
        if self.Planet.xLocatexm < 0 and self.Planet.yLocatexm < 0:
            return -v * siny
        if self.Planet.xLocatexm > 0 and self.Planet.yLocatexm < 0:
            return +v * siny

    def Move(self, time=3600 * 24):
        ax = self.Gravitational_Forcex() / self.Planet.Massxkg
        ay = self.Gravitational_Forcey() / self.Planet.Massxkg

        self.Vx() = self.Vx() + time * ax
        self.Vy() = self.Vy() + time * ay

        self.Planet.xLocatexm += self.Vx() * time
        self.Planet.yLocatexm += self.Vy() * time

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

x_dünya = []
y_dünya = []


def update(frame):
    Sistem.Move()

    x_gecmis.append(Sistem.Planet.xLocatexm)
    y_gecmiş.append(Sistem.Planet.yLocatexm)

    x_dünya = Sistem.Planet.xLocatexm
    y_dünya = Sistem.Planet.yLocatexm


fig, ax = plt.subplots(figsize=(7, 7))
ax.set_xlim(-2e11, 2e11)
ax.set_ylim(-2e11, 2e11)
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)

gunes = ax.plot(0, 0, "yo", markersize=10, label="Güneş")
dünya = ax.plot(x_dünya, y_dünya, "bo", markersize=6, label="Dünya")
yorunge = ax.plot([], [], "b--", alpha=0.4, linewidth=1)


ani = FuncAnimation(fig, update, frames=120, interval=20, blit=True)

plt.legend()
plt.show()
