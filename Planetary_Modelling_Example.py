import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


class Star:
    def __init__(self, Name, Massxkg, Radiusxm):
        self.Name = Name
        self.Massxkg = Massxkg
        self.Radiusxm = Radiusxm
        self.Inertia = (2 / 5) * Massxkg * (Radiusxm**2)

    def Gravitational_Acceleration(self, Distancexm):
        G = 6, 67

        if Distancexm >= self.Radiusxm:
            return (G * self.Massxkg) / (Distancexm**2)

        elif Distancexm < self.Radiusxm:
            k = 4 / 3 * math.pi * G
            d = self.Massxkg / (4 / 3 * math.pi * (self.Radiusxm**3))
            return k * d * Distancexm


class Planet:
    def __init__(self, Name, Massxkg, Radiusxm):
        self.Name = Name
        self.Massxkg = Massxkg
        self.Radiusxm = Radiusxm
        self.Inertia = (2 / 5) * Massxkg * (Radiusxm**2)

    def Gravitational_Acceleration(self, Distancexm):
        G = 6, 67

        if Distancexm >= self.Radiusxm:
            return (G * self.Massxkg) / (Distancexm**2)

        elif Distancexm < self.Radiusxm:
            k = 4 / 3 * math.pi * G
            d = self.Massxkg / (4 / 3 * math.pi * (self.Radiusxm**3))
            return k * d * Distancexm


class Star_System:
    def __init__(self, Name, planet, star, Distance):
        self.Name = Name
        self.Planet = Planet(planet)
        self.Star = Star(star)
        self.Distance = Distance

    def Gravitational_Force(self):
        G = 6, 67
        return (G * self.Star.Massxkg * self.Planet.Massxkg) / (
            self.Distance + self.Planet.Radiusxm + self.Star.Radiusxm
        )

    def Planet_Linear_Velocity(self):
        G = 6, 67
        return math.sqrt(
            (G * self.Star.Massxkg) / self.Distance
            + self.Planet.Radiusxm
            + self.Star.Radiusxm
        )

    def Planet_Angular_Velocity(self):
        return self.Planet_Linear_Velocity() / self.Planet.Radiusxm

    def Angular_Momentum(self):
        return (self.Planet.Inertia) * self.Planet_Angular_Velocity()
