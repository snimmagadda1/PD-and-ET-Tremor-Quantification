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
        butter_lowpass_IIR_filter, integrate_time_series, gs_to_accel
    from package_data import extrapolate_accel_data_testing

    import numpy as np
    import matplotlib.pyplot as plt

    fs = 115
    x_accel, y_accel, z_accel = extrapolate_accel_data_testing('sinusoid_14hz_fs_115.txt')

    # remove high frequencies
    x_filt = butter_lowpass_IIR_filter(x_accel,  15, 44)
    y_filt = butter_lowpass_IIR_filter(y_accel,  15, 44)
    z_filt = butter_lowpass_IIR_filter(z_accel,  15, 44)
    time = np.arange(0, len(x_filt), 1) / float(fs)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_rawg = calculate_magnitude_acceleration(x_accel, y_accel, z_accel)
    acceleration_raw_no_gravg = remove_gravity_ENMO(x_accel, y_accel, z_accel)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filteredg = calculate_magnitude_acceleration(x_filt, y_filt, z_filt)
    acceleration_filtered_no_gravg = remove_gravity_ENMO(x_filt, y_filt, z_filt)

    # remove gravity
    acceleration_raw = gs_to_accel(acceleration_rawg)
    acceleration_raw_no_grav = gs_to_accel(acceleration_raw_no_gravg)
    acceleration_filtered = gs_to_accel(acceleration_filteredg)
    acceleration_filtered_no_grav = gs_to_accel(acceleration_filtered_no_gravg)

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
        butter_lowpass_IIR_filter, integrate_time_series, gs_to_accel
    from package_data import extrapolate_accel_data_testing

    import numpy as np
    import matplotlib.pyplot as plt

    fs = 115
    x_accel, y_accel, z_accel = extrapolate_accel_data_testing('sinusoid_8hz_fs_115.txt')

    # remove high frequencies
    x_filt = butter_lowpass_IIR_filter(x_accel,  14, 44)
    y_filt = butter_lowpass_IIR_filter(y_accel,  14, 44)
    z_filt = butter_lowpass_IIR_filter(z_accel,  14, 44)
    time = np.arange(0, len(x_filt), 1) / float(fs)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_rawg = calculate_magnitude_acceleration(x_accel, y_accel, z_accel)
    acceleration_raw_no_gravg = remove_gravity_ENMO(x_accel, y_accel, z_accel)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filteredg = calculate_magnitude_acceleration(x_filt, y_filt, z_filt)
    acceleration_filtered_no_gravg = remove_gravity_ENMO(x_filt, y_filt, z_filt)

    # remove gravity
    acceleration_raw = gs_to_accel(acceleration_rawg)
    acceleration_raw_no_grav = gs_to_accel(acceleration_raw_no_gravg)
    acceleration_filtered = gs_to_accel(acceleration_filteredg)
    acceleration_filtered_no_grav = gs_to_accel(acceleration_filtered_no_gravg)

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
        butter_lowpass_IIR_filter, integrate_time_series, gs_to_accel
    from package_data import extrapolate_accel_data_testing

    import numpy as np
    import matplotlib.pyplot as plt

    fs = 115
    x_accel, y_accel, z_accel = extrapolate_accel_data_testing('sinusoid_2hz_fs_115.txt')

    # remove high frequencies
    x_filt = butter_lowpass_IIR_filter(x_accel,  14, 44)
    y_filt = butter_lowpass_IIR_filter(y_accel,  14, 44)
    z_filt = butter_lowpass_IIR_filter(z_accel,  14, 44)
    time = np.arange(0, len(x_filt), 1) / float(fs)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_rawg = calculate_magnitude_acceleration(x_accel, y_accel, z_accel)
    acceleration_raw_no_gravg = remove_gravity_ENMO(x_accel, y_accel, z_accel)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filteredg = calculate_magnitude_acceleration(x_filt, y_filt, z_filt)
    acceleration_filtered_no_gravg = remove_gravity_ENMO(x_filt, y_filt, z_filt)

    # remove gravity
    acceleration_raw = gs_to_accel(acceleration_rawg)
    acceleration_raw_no_grav = gs_to_accel(acceleration_raw_no_gravg)
    acceleration_filtered = gs_to_accel(acceleration_filteredg)
    acceleration_filtered_no_grav = gs_to_accel(acceleration_filtered_no_gravg)

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
        butter_lowpass_IIR_filter, integrate_time_series, gs_to_accel
    from package_data import extrapolate_accel_data_testing

    import numpy as np
    import matplotlib.pyplot as plt

    fs = 115
    x_g, y_g, z_g = extrapolate_accel_data_testing('sinusoid_0hz_fs_115.txt')

    # remove high frequencies
    x_filt = butter_lowpass_IIR_filter(x_g,  14, 44)
    y_filt = butter_lowpass_IIR_filter(y_g,  14, 44)
    z_filt = butter_lowpass_IIR_filter(z_g,  14, 44)
    time = np.arange(0, len(x_filt), 1) / float(fs)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_rawg = calculate_magnitude_acceleration(x_g, y_g, z_g)
    acceleration_raw_no_gravg = remove_gravity_ENMO(x_g, y_g, z_g)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filteredg = calculate_magnitude_acceleration(x_filt, y_filt, z_filt)
    acceleration_filtered_no_gravg = remove_gravity_ENMO(x_filt, y_filt, z_filt)

    # remove gravity
    acceleration_raw = gs_to_accel(acceleration_rawg)
    acceleration_raw_no_grav = gs_to_accel(acceleration_raw_no_gravg)
    acceleration_filtered = gs_to_accel(acceleration_filteredg)
    acceleration_filtered_no_grav = gs_to_accel(acceleration_filtered_no_gravg)

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
        butter_lowpass_IIR_filter, integrate_time_series, gs_to_accel
    from package_data import extrapolate_accel_data_testing

    import numpy as np
    import matplotlib.pyplot as plt

    fs = 115
    x_accel, y_accel, z_accel = extrapolate_accel_data_testing('sinusoid_8hz_fs_115.txt')

    # remove high frequencies
    x_filt = butter_lowpass_IIR_filter(x_accel, 14, 44)
    y_filt = butter_lowpass_IIR_filter(y_accel, 14, 44)
    z_filt = butter_lowpass_IIR_filter(z_accel, 14, 44)
    time = np.arange(0, len(x_filt), 1) / float(fs)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_rawg = calculate_magnitude_acceleration(x_accel, y_accel, z_accel)
    acceleration_raw_no_gravg = remove_gravity_ENMO(x_accel, y_accel, z_accel)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filteredg = calculate_magnitude_acceleration(x_filt, y_filt, z_filt)
    acceleration_filtered_no_gravg = remove_gravity_ENMO(x_filt, y_filt, z_filt)

    # remove gravity
    acceleration_raw = gs_to_accel(acceleration_rawg)
    acceleration_raw_no_grav = gs_to_accel(acceleration_raw_no_gravg)
    acceleration_filtered = gs_to_accel(acceleration_filteredg)
    acceleration_filtered_no_grav = gs_to_accel(acceleration_filtered_no_gravg)

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


def test_welch_8hz():
    """Test welch method of PSD estimation visually

    :return:
    """

    from process_data import remove_gravity_ENMO, \
        calculate_magnitude_acceleration, \
        butter_lowpass_IIR_filter, integrate_time_series, \
        gs_to_accel, psd_welch, is_tremor
    from package_data import extrapolate_accel_data_testing

    import numpy as np
    import matplotlib.pyplot as plt

    fs = 115
    x_accel, y_accel, z_accel = extrapolate_accel_data_testing('sinusoid_8hz_fs_115.txt')

    # remove high frequencies
    x_filt = butter_lowpass_IIR_filter(x_accel, 14, 44)
    y_filt = butter_lowpass_IIR_filter(y_accel, 14, 44)
    z_filt = butter_lowpass_IIR_filter(z_accel, 14, 44)
    time = np.arange(0, len(x_filt), 1) / float(fs)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_rawg = calculate_magnitude_acceleration(x_accel, y_accel, z_accel)
    acceleration_raw_no_gravg = remove_gravity_ENMO(x_accel, y_accel, z_accel)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filteredg = calculate_magnitude_acceleration(x_filt, y_filt, z_filt)
    acceleration_filtered_no_gravg = remove_gravity_ENMO(x_filt, y_filt, z_filt)

    # remove gravity
    acceleration_raw = gs_to_accel(acceleration_rawg)
    acceleration_raw_no_grav = gs_to_accel(acceleration_raw_no_gravg)
    acceleration_filtered = gs_to_accel(acceleration_filteredg)
    acceleration_filtered_no_grav = gs_to_accel(acceleration_filtered_no_gravg)

    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 256)

    # test if tremor present in segment
    alert = is_tremor(f, pxx)
    print(alert)

    f1 = plt.figure()
    ax1 = f1.add_subplot(111)
    ax1.semilogy(f, pxx, color='r')
    plt.xlabel('Frequency (HZ)')
    plt.ylabel('PSD [V**2/Hz]')
    plt.title('PSD of 8 Hz Sinusoid ADXL345 Data')
    f1.savefig('8hz_PSD.png')
    plt.show()


def test_welch_2hz():
    """Test welch method of PSD estimation visually

    :return:
    """

    from process_data import remove_gravity_ENMO, \
        calculate_magnitude_acceleration, \
        butter_lowpass_IIR_filter, integrate_time_series, gs_to_accel, \
        psd_welch, is_tremor
    from package_data import extrapolate_accel_data_testing

    import numpy as np
    import matplotlib.pyplot as plt

    fs = 115
    x_accel, y_accel, z_accel = extrapolate_accel_data_testing('sinusoid_2hz_fs_115.txt')

    # remove high frequencies
    x_filt = butter_lowpass_IIR_filter(x_accel, 14, 44)
    y_filt = butter_lowpass_IIR_filter(y_accel, 14, 44)
    z_filt = butter_lowpass_IIR_filter(z_accel, 14, 44)
    time = np.arange(0, len(x_filt), 1) / float(fs)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_rawg = calculate_magnitude_acceleration(x_accel, y_accel, z_accel)
    acceleration_raw_no_gravg = remove_gravity_ENMO(x_accel, y_accel, z_accel)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filteredg = calculate_magnitude_acceleration(x_filt, y_filt, z_filt)
    acceleration_filtered_no_gravg = remove_gravity_ENMO(x_filt, y_filt, z_filt)

    # remove gravity
    acceleration_raw = gs_to_accel(acceleration_rawg)
    acceleration_raw_no_grav = gs_to_accel(acceleration_raw_no_gravg)
    acceleration_filtered = gs_to_accel(acceleration_filteredg)
    acceleration_filtered_no_grav = gs_to_accel(acceleration_filtered_no_gravg)

    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 256)

    # test if tremor present in segment
    alert = is_tremor(f, pxx)
    print(alert)

    f1 = plt.figure()
    ax1 = f1.add_subplot(111)
    ax1.semilogy(f, pxx, color='r')
    plt.xlabel('Frequency (HZ)')
    plt.ylabel('PSD [V**2/Hz]')
    plt.title('PSD of 2 Hz Sinusoid ADXL345 Data')
    f1.savefig('2hz_PSD.png')
    plt.show()


def iteratively_test_welch_methods():
    """Test welch method window length on a 14 Hz sinusoid

        :return:
        """
    from process_data import remove_gravity_ENMO, \
        calculate_magnitude_acceleration, \
        butter_lowpass_IIR_filter, integrate_time_series, \
        gs_to_accel, psd_welch, get_DF
    from package_data import extrapolate_accel_data_testing

    import numpy as np
    import matplotlib.pyplot as plt

    fs = 115
    fc =14
    x_accel, y_accel, z_accel = extrapolate_accel_data_testing('sinusoid_2hz_fs_115.txt')

    # remove high frequencies
    x_filt = butter_lowpass_IIR_filter(x_accel, fc, fs)
    y_filt = butter_lowpass_IIR_filter(y_accel, fc, fs)
    z_filt = butter_lowpass_IIR_filter(z_accel, fc, fs)
    time = np.arange(0, len(x_filt), 1) / float(fs)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_rawg = calculate_magnitude_acceleration(x_accel, y_accel, z_accel)
    acceleration_raw_no_gravg = remove_gravity_ENMO(x_accel, y_accel, z_accel)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filteredg = calculate_magnitude_acceleration(x_filt, y_filt, z_filt)
    acceleration_filtered_no_gravg = remove_gravity_ENMO(x_filt, y_filt, z_filt)

    # remove gravity
    acceleration_raw = gs_to_accel(acceleration_rawg)
    acceleration_raw_no_grav = gs_to_accel(acceleration_raw_no_gravg)
    acceleration_filtered = gs_to_accel(acceleration_filteredg)
    acceleration_filtered_no_grav = gs_to_accel(acceleration_filtered_no_gravg)

    # plot different window lengths
    fig= plt.figure(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')
    plt.subplot(331)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 40)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x,y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD [V**2/Hz]')
    plt.title('40')

    plt.subplot(332)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 80)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x, y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD [V**2/Hz]')
    plt.title('80')

    plt.subplot(333)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 120)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x, y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD [V**2/Hz]')
    plt.title('120')

    plt.subplot(334)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 160)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x, y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD [V**2/Hz]')
    plt.title('160')

    plt.subplot(335)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 200)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x, y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD [V**2/Hz]')
    plt.title('200')

    plt.subplot(336)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 240)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x, y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD [V**2/Hz]')
    plt.title('240')

    plt.subplot(337)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 280)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x, y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD [V**2/Hz]')
    plt.title('280')

    plt.subplot(338)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 320)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x, y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD [V**2/Hz]')
    plt.title('320')

    plt.subplot(339)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 360)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x, y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD [V**2/Hz]')
    plt.title('360')
    plt.tight_layout()
    plt.savefig('welch_windows_2hz.png')

    plt.show()



if __name__ == "__main__":
    test_welch_8hz()


    pass










