import pandas as pd
import numpy as np

Data_Planets = pd.read_csv("planets.csv")

Data_Planets["Massxkg"] = Data_Planets["Mass (10^24kg)"] * 1e24
Data_Planets["Radiusxm"] = Data_Planets["Diameter (km)"] * 1e3 / 2
Data_Planets["Distancexm"] = Data_Planets["Distance from Sun (10^6 km)"] * 1e6 * 1e3

Data_Planets = Data_Planets[["Planet", "Massxkg", "Radiusxm", "Distancexm"]]
print(Data_Planets)
