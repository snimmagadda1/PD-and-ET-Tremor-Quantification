def extrapolate_accel_data(filename):
    x = []
    y = []
    z = []

    with open(filename, 'r') as f:
        alllines = f.readlines()
        for line in alllines:
            components = line.split(',')
            sep = ';'
            cleaned_z = components[2].split(sep,1)[0]
            components[2] = cleaned_z
            x.append(float(components[0]))
            y.append(float(components[1]))
            z.append(float(components[2]))
    return x, y, z


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np
    from process_data import accel_to_velocity, velocity_to_displacement
    import pandas as pd

    # sampling frequency of test data
    fs = 44
    x, y, z = extrapolate_accel_data("rawacceldata.txt")
    entry_numbers = list(range(0, len(x)))
    time = []
    for item in entry_numbers:
        time.append(item/fs)







