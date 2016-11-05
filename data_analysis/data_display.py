"""This is a testing file for displaying plots for
troubleshooting / analysis
"""



def test_14hz_sampling():
    """ Plotting initial data using lowpass filter and ENMO to remove gravity.
    ** not a unit test **

    :return: visual plots
    """
    from process_data import remove_gravity_ENMO, \
        calculate_magnitude_acceleration,\
        butter_lowpass_filter, integrate_time_series, gs_to_accel
    from package_data import extrapolate_accel_data_testing

    import numpy as np
    import matplotlib.pyplot as plt

    fs = 115
    x_accel, y_accel, z_accel = extrapolate_accel_data_testing('sinusoid_14hz_fs_115.txt')

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

    # plot raw acceleration without gravity
    f1 = plt.figure()
    ax1 = f1.add_subplot(111)
    ax1.plot(time[0:400], acceleration_raw_no_grav[0:400], color='r')
    plt.xlabel('time (s)')
    plt.ylabel('acceleration (m/s^2)')
    plt.title('Raw Sinusoid @ 14 Hz -- fs = 115 Hz')
    f1.savefig('14hz_sinusoid_raw.png')


    # plot filtered acceleration without gravity
    f2 = plt.figure()
    ax1 = f2.add_subplot(111)
    ax1.plot(time[0:400], acceleration_filtered_no_grav[0:400], color='g')
    plt.xlabel('time (s)')
    plt.ylabel('acceleration (m/s^2)')
    plt.title('Filtered Sinusoid @ 14 Hz -- fs = 115 Hz')
    f2.savefig('14hz_sinusoid_filtered.png')

    plt.show()


def test_8hz_sampling():
    """ Plotting initial data using lowpass filter and ENMO to remove gravity.
    ** not a unit test **

    :return: visual plots
    """
    from process_data import remove_gravity_ENMO, \
        calculate_magnitude_acceleration,\
        butter_lowpass_filter, integrate_time_series, gs_to_accel
    from package_data import extrapolate_accel_data_testing

    import numpy as np
    import matplotlib.pyplot as plt

    fs = 115
    x_accel, y_accel, z_accel = extrapolate_accel_data_testing('sinusoid_8hz_fs_115.txt')

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

    # plot raw acceleration without gravity
    f1 = plt.figure()
    ax1 = f1.add_subplot(111)
    ax1.plot(time[0:400], acceleration_raw_no_grav[0:400], color='r')
    plt.xlabel('time (s)')
    plt.ylabel('acceleration (m/s^2)')
    plt.title('Raw Sinusoid @ 8 Hz -- fs = 115 Hz')
    f1.savefig('8hz_sinusoid_raw.png')


    # plot filtered acceleration without gravity
    f2 = plt.figure()
    ax1 = f2.add_subplot(111)
    ax1.plot(time[0:400], acceleration_filtered_no_grav[0:400], color='g')
    plt.xlabel('time (s)')
    plt.ylabel('acceleration (m/s^2)')
    plt.title('Filtered Sinusoid @ 8 Hz -- fs = 115 Hz')
    f2.savefig('8hz_sinusoid_filtered.png')

    plt.show()


def test_2hz_sampling():
    """ Plotting initial data using lowpass filter and ENMO to remove gravity.
    ** not a unit test **

    :return: visual plots
    """
    from process_data import remove_gravity_ENMO, \
        calculate_magnitude_acceleration,\
        butter_lowpass_filter, integrate_time_series, gs_to_accel
    from package_data import extrapolate_accel_data_testing

    import numpy as np
    import matplotlib.pyplot as plt

    fs = 115
    x_accel, y_accel, z_accel = extrapolate_accel_data_testing('sinusoid_2hz_fs_115.txt')

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

    # plot raw acceleration without gravity
    f1 = plt.figure()
    ax1 = f1.add_subplot(111)
    ax1.plot(time[0:400], acceleration_raw_no_grav[0:400], color='r')
    plt.xlabel('time (s)')
    plt.ylabel('acceleration (m/s^2)')
    plt.title('Raw Sinusoid @ 2 Hz -- fs = 115 Hz')
    f1.savefig('2hz_sinusoid_raw.png')


    # plot filtered acceleration without gravity
    f2 = plt.figure()
    ax1 = f2.add_subplot(111)
    ax1.plot(time[0:400], acceleration_filtered_no_grav[0:400], color='g')
    plt.xlabel('time (s)')
    plt.ylabel('acceleration (m/s^2)')
    plt.title('Filtered Sinusoid @ 2 Hz -- fs = 115 Hz')
    f2.savefig('2hz_sinusoid_filtered.png')

    plt.show()


def test_0hz_sampling():
    """ Plotting initial data using lowpass filter and ENMO to remove gravity.
    ** not a unit test **

    :return: visual plots
    """
    from process_data import remove_gravity_ENMO, \
        calculate_magnitude_acceleration,\
        butter_lowpass_filter, integrate_time_series, gs_to_accel
    from package_data import extrapolate_accel_data_testing

    import numpy as np
    import matplotlib.pyplot as plt

    fs = 115
    x_g, y_g, z_g = extrapolate_accel_data_testing('sinusoid_0hz_fs_115.txt')

    # remove high frequencies
    x_filt = butter_lowpass_filter(x_g,  15, 44)
    y_filt = butter_lowpass_filter(y_g,  15, 44)
    z_filt = butter_lowpass_filter(z_g,  15, 44)
    time = np.arange(0, len(x_filt), 1) / float(fs)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_raw = calculate_magnitude_acceleration(x_g, y_g, z_g)
    acceleration_raw_no_grav = remove_gravity_ENMO(x_g, y_g, z_g)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filtered = calculate_magnitude_acceleration(x_filt, y_filt, z_filt)
    acceleration_filtered_no_grav = remove_gravity_ENMO(x_filt, y_filt, z_filt)

    # plot raw acceleration without gravity
    f1 = plt.figure()
    ax1 = f1.add_subplot(111)
    ax1.plot(time[0:400], acceleration_raw_no_grav[0:400], color='r')
    plt.xlabel('time (s)')
    plt.ylabel('acceleration (m/s^2)')
    plt.title('Raw Sinusoid @ 0 Hz -- fs = 115 Hz')
    f1.savefig('0hz_sinusoid_raw.png')

    # plot filtered acceleration without gravity
    f2 = plt.figure()
    ax1 = f2.add_subplot(111)
    ax1.plot(time[0:400], acceleration_filtered_no_grav[0:400], color='g')
    plt.xlabel('time (s)')
    plt.ylabel('acceleration (m/s^2)')
    plt.title('Filtered Sinusoid @ 0 Hz -- fs = 115 Hz')
    f2.savefig('0hz_sinusoid_filtered.png')

    plt.show()


def display_integrations():
    """Display the result of integrating to find velocity and displacement

        :return: visual plots
        """
    from process_data import remove_gravity_ENMO, \
        calculate_magnitude_acceleration, \
        butter_lowpass_filter, integrate_time_series, gs_to_accel
    from package_data import extrapolate_accel_data_testing

    import numpy as np
    import matplotlib.pyplot as plt

    fs = 115
    x_accel, y_accel, z_accel = extrapolate_accel_data_testing('sinusoid_8hz_fs_115.txt')

    # remove high frequencies
    x_filt = butter_lowpass_filter(x_accel, 15, 44)
    y_filt = butter_lowpass_filter(y_accel, 15, 44)
    z_filt = butter_lowpass_filter(z_accel, 15, 44)
    time = np.arange(0, len(x_filt), 1) / float(fs)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_raw = calculate_magnitude_acceleration(x_accel, y_accel, z_accel)
    acceleration_raw_no_grav = remove_gravity_ENMO(x_accel, y_accel, z_accel)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filtered = calculate_magnitude_acceleration(x_filt, y_filt, z_filt)
    acceleration_filtered_no_grav = remove_gravity_ENMO(x_filt, y_filt, z_filt)

    velocity_filtered = integrate_time_series(acceleration_filtered, time, fs)

    # plot raw acceleration without gravity
    f1 = plt.figure()
    ax1 = f1.add_subplot(111)
    ax1.plot(time[0:400], velocity_filtered[0:400], color='r')
    ax1.plot(time[0:400], acceleration_filtered[0:400], color='g')
    plt.xlabel('time (s)')
    plt.ylabel('Velocity (m/s^2)')
    plt.title('Velocity of 8 Hz Test Sinusoid')

    plt.show()


def troubleshoot_integrations():
    """Make sure integration is outputting as expected

    :return: visual plots
    """
    import numpy as np
    from process_data import integrate_time_series
    import matplotlib.pyplot as plt

    t = np.arange(0.0, 1.0, 0.01)
    y = np.sin(2*np.pi*t)

    y_int = integrate_time_series(t, y, 0)

    fig = plt.figure(1)

    ax1 = fig.add_subplot(111)
    ax1.plot(t, y)
    ax1.plot(t, y_int, color='r')
    ax1.grid(True)
    ax1.set_ylim((-2, 2))
    ax1.set_ylabel('1 Hz')
    ax1.set_title('A sine wave or two')

    plt.show()


def test_welch():
    """Test welch method of PSD estimation visually

    :return:
    """



if __name__ == "__main__":
    test_0hz_sampling()
    test_2hz_sampling()
    test_8hz_sampling()
    test_14hz_sampling()

    pass










