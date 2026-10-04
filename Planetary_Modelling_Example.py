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
    def __init__(self, Name, Massxkg, Radiusxm, xLocatexm):
        self.Name = Name
        self.Massxkg = Massxkg
        self.Radiusxm = Radiusxm
        self.Inertia = (2 / 5) * Massxkg * (Radiusxm**2)
        self.xLocatexm = xLocatexm
        self.yLocatexm = 0

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


# Stars and Planets


Güneş = Star(
    "Güneş",
    2e30,
    696.300e3,
)

Planet1 = Planet("Planet1", 0, 0, 0)


import Planets_and_Stars as ps

Data = ps.Data_Planets

Planet_input = input(
    "Enter the name of the planet(Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune): "
)

if Planet_input.lower() == "mercury":
    Planet1 = Planet(
        "Planet1",
        Data.iloc[0]["Massxkg"],
        Data.iloc[0]["Radiusxm"],
        Data.iloc[0]["Distancexm"],
    )
    color = "gray"
if Planet_input.lower() == "venus":
    Planet1 = Planet(
        "Planet1",
        Data.iloc[1]["Massxkg"],
        Data.iloc[1]["Radiusxm"],
        Data.iloc[1]["Distancexm"],
    )
    color = "chocolate"
if Planet_input.lower() == "earth":
    Planet1 = Planet(
        "Planet1",
        Data.iloc[2]["Massxkg"],
        Data.iloc[2]["Radiusxm"],
        Data.iloc[2]["Distancexm"],
    )
    color = "blue"
if Planet_input.lower() == "mars":
    Planet1 = Planet(
        "Planet1",
        Data.iloc[3]["Massxkg"],
        Data.iloc[3]["Radiusxm"],
        Data.iloc[3]["Distancexm"],
    )
    color = "red"
if Planet_input.lower() == "jupiter":
    Planet1 = Planet(
        "Planet1",
        Data.iloc[4]["Massxkg"],
        Data.iloc[4]["Radiusxm"],
        Data.iloc[4]["Distancexm"],
    )
    color = "navajowhite"
if Planet_input.lower() == "saturn":
    Planet1 = Planet(
        "Planet1",
        Data.iloc[5]["Massxkg"],
        Data.iloc[5]["Radiusxm"],
        Data.iloc[5]["Distancexm"],
    )
    color = "peru"
if Planet_input.lower() == "uranus":
    Planet1 = Planet(
        "Planet1",
        Data.iloc[6]["Massxkg"],
        Data.iloc[6]["Radiusxm"],
        Data.iloc[6]["Distancexm"],
    )
    color = "lightblue"
if Planet_input.lower() == "neptune":
    Planet1 = Planet(
        "Planet1",
        Data.iloc[7]["Massxkg"],
        Data.iloc[7]["Radiusxm"],
        Data.iloc[7]["Distancexm"],
    )
    color = "darkblue"

# Simulation

System = Star_System("Star_System", Planet1, Güneş)

x_past, y_past = [], []

fig, ax = plt.subplots(figsize=(12, 12))
ax.set_xlim(-1.5 * Planet1.xLocatexm, 1.5 * Planet1.xLocatexm)
ax.set_ylim(-1.5 * Planet1.xLocatexm, 1.5 * Planet1.xLocatexm)
ax.set_aspect("equal")
ax.grid(True, alpha=0.3)

(star,) = ax.plot(0, 0, "yo", markersize=30, label="Star")
(planet,) = ax.plot([], [], color=color, marker="o", markersize=5, label="Planet")
(orbit,) = ax.plot([], [], "k--", alpha=0.4, linewidth=1)


def update(frame):
    for i in range(10):
        System.Move()

    x_past.append(System.Planet.xLocatexm)
    y_past.append(System.Planet.yLocatexm)

    planet.set_data([System.Planet.xLocatexm], [System.Planet.yLocatexm])
    orbit.set_data(x_past, y_past)

    return planet, orbit


ani = FuncAnimation(fig, update, frames=240, interval=20, blit=False)

plt.legend()
plt.show()
