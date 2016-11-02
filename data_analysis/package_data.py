
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


def test_initial_data():
    from process_data import remove_gravity_ENMO, \
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

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_raw = calculate_magnitude_acceleration(x, y, z)
    acceleration_raw_no_grav = remove_gravity_ENMO(x, y, z)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filtered = calculate_magnitude_acceleration(x_filt, y_filt, z_filt)
    acceleration_filtered_no_grav = remove_gravity_ENMO(x_filt, y_filt, z_filt)

    # Plot data
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 8), sharey=True)
    axes[0, 0].set_ylabel('Acceleration (m/s^2')
    axes[0, 0].set_xlabel('Time s')
    axes[0, 1].set_xlabel('Time s')
    axes[1, 0].set_ylabel('Acceleration (m/s^2')
    axes[1, 0].set_xlabel('Time s')
    axes[1, 1].set_xlabel('Time s')

    axes[0, 0].set_title('Raw acceleration')
    axes[0, 1].set_title('Filtered acceleration')
    axes[1, 0].set_title('Raw acceleration w/out grav')
    axes[1, 1].set_title('Filtered acceleration w/out grav')

    axes[0, 0].plot(time, acceleration_raw, color='r')
    axes[0, 1].plot(time, acceleration_filtered, color='g')

    axes[1, 0].plot(time, acceleration_raw_no_grav, color='r')
    axes[1, 1].plot(time, acceleration_filtered_no_grav, color='g')
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    test_initial_data()

