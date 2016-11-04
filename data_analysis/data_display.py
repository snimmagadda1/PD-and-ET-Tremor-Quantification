def test_initial_data():
    """ Plotting initial data using lowpass filter and ENMO to remove gravity.
    ** not a unit test **

    :return: visual plots
    """
    from process_data import remove_gravity_ENMO, \
        calculate_magnitude_acceleration,\
        butter_lowpass_filter, integrate_time_series, gs_to_accel
    from package_data import extrapolate_accel_data

    import numpy as np
    import matplotlib.pyplot as plt

    fs = 115
    x_g, y_g, z_g = extrapolate_accel_data('sinusoid_14hz_fs_115.txt')
    x_accel, y_accel, z_accel = gs_to_accel(x_g, y_g, z_g)

    # remove high frequencies
    x_filt = butter_lowpass_filter(x_accel,  15, 44)
    y_filt = butter_lowpass_filter(y_accel,  15, 44)
    z_filt = butter_lowpass_filter(z_accel,  15, 44)
    time = np.arange(0, len(x_filt), 1) / float(fs)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_raw = calculate_magnitude_acceleration(x_accel, y_accel, z_accel)
    acceleration_raw_no_grav = remove_gravity_ENMO(x_accel, y_accel, z_accel)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filtered = calculate_magnitude_acceleration(x_filt, y_filt, z_filt)
    acceleration_filtered_no_grav = remove_gravity_ENMO(x_filt, y_filt, z_filt)

    velocity_filtered = integrate_time_series(acceleration_filtered, fs)
    displacement_filtered = integrate_time_series(velocity_filtered, fs)

    # plot raw acceleration without gravity
    f1 = plt.figure()
    ax1 = f1.add_subplot(111)
    ax1.plot(time[0:400], acceleration_raw_no_grav[0:400], color='r')

    # plot filtered acceleration without gravity
    f1 = plt.figure()
    ax1 = f1.add_subplot(111)
    ax1.plot(time[0:400], acceleration_filtered_no_grav[0:400], color='g')

    plt.show()



if __name__ == "__main__":
    test_initial_data()









