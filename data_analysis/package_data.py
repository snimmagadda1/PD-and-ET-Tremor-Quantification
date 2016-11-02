
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
    from process_data import integrate_time_series, remove_gravity_ENMO, calculate_magnitude_acceleration
    import numpy as np
    import matplotlib.pyplot as plt
    import math


    fs = 44
    x, y, z = extrapolate_accel_data('rawacceldata.txt')
    acceleration = calculate_magnitude_acceleration(x, y, z)
    acceleration_no_grav = remove_gravity_ENMO(x, y, z)
    velocity = integrate_time_series(acceleration_no_grav, fs)



    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(16,8))
    plt.tight_layout()

    # x data
    # axes[0, 0].plot(time, x, color='r')
    # axes[1, 0].plot(time, x_velo, color='r')
    #
    # plt.show()


    pass