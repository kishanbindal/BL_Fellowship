def windChill(f,v):
    if (f > 50) or (v<3 or v>120):
        raise ValueError("Value of temp has to be below 50 and windspeed should be between 3mph and 120mph only!")
    else:
        w = 35.74 + 0.6215 * f + (0.4275 * f - 35.75) * (v) ** 0.16
        return round(w, 2)

print(windChill(48.5,31.8))
