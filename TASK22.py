melt = {"Ag2O": 160, "Al2O3": 2053, "O2": 218, "AsH3": 117, "B2O3": 450}
melting_temperatures = []
for compound, temperature in melt.items():
    if compound.endswith("O"):
        melting_temperatures.append(str(temperature))
print(" ".join(melting_temperatures))
