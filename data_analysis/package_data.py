
def extrapolate_accel_data(filename):
    x = []
    y = []
    z = []
    import numpy as np
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
    return np.array(x), np.array(y), np.array(z)



if __name__ == "__main__":
    from process_data import integrate_time_series, remove_gravity_ENMO, \
        calculate_magnitude_acceleration, butter_bandpass_filter
    import numpy as np
    import matplotlib.pyplot as plt
    import math


    fs = 44
    x, y, z = extrapolate_accel_data('rawacceldata.txt')

    # remove high frequencies
    x_filt = butter_bandpass_filter(x, 0, 12, 44)
    y_filt = butter_bandpass_filter(y, 0, 12, 44)
    z_filt = butter_bandpass_filter(z, 0, 12, 44)
    time = np.array(range(0, len(x_filt))) / fs

    # calculate magnitude of acceleration with and without grav
    acceleration = calculate_magnitude_acceleration(x_filt, y_filt, z_filt)
    acceleration_no_grav = remove_gravity_ENMO(x_filt, y_filt, z_filt)
    velocity = integrate_time_series(acceleration_no_grav, fs)

    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(16,8), sharey=True)
    plt.tight_layout()

    axes[0].plot(time, acceleration, color='r')
    axes[1].plot(time, acceleration_no_grav, color='g')

    plt.show()


    pass