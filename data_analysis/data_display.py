def test_initial_data():
    from process_data import remove_gravity_ENMO, \
        calculate_magnitude_acceleration, butter_lowpass_filter
    from package_data import extrapolate_accel_data

    import numpy as np
    import matplotlib.pyplot as plt

    fs = 44
    x, y, z = extrapolate_accel_data('rawacceldata.txt')

    # remove high frequencies
    x_filt = butter_lowpass_filter(x,  12, 44)
    y_filt = butter_lowpass_filter(y,  12, 44)
    z_filt = butter_lowpass_filter(z,  12, 44)
    time = np.arange(0, len(x_filt), 1) / float(fs)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_raw = calculate_magnitude_acceleration(x, y, z)
    acceleration_raw_no_grav = remove_gravity_ENMO(x, y, z)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filtered = calculate_magnitude_acceleration(x_filt, y_filt, z_filt)
    acceleration_filtered_no_grav = remove_gravity_ENMO(x_filt, y_filt, z_filt)

    # Plot data
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 8), sharey=True)
    axes[0, 0].set_ylabel('Acceleration (m/s^2)')
    axes[0, 0].set_xlabel('Time s')
    axes[0, 1].set_xlabel('Time s')
    axes[1, 0].set_ylabel('Acceleration (m/s^2)')
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









