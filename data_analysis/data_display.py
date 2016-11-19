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
    x_accel, y_accel, z_accel = extrapolate_accel_data_testing('sinusoid_8hz_fs_115.txt')

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
    plt.ylabel('PSD (m/s$^2$)$^2$/Hz]')
    plt.title('40')

    plt.subplot(332)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 80)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x, y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD (m/s$^2$)$^2$/Hz]')
    plt.title('80')

    plt.subplot(333)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 120)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x, y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD (m/s$^2$)$^2$/Hz]')
    plt.title('120')

    plt.subplot(334)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 160)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x, y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD (m/s$^2$)$^2$/Hz]')
    plt.title('160')

    plt.subplot(335)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 200)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x, y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD (m/s$^2$)$^2$/Hz]')
    plt.title('200')

    plt.subplot(336)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 240)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x, y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD (m/s$^2$)$^2$/Hz]')
    plt.title('240')

    plt.subplot(337)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 280)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x, y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD (m/s$^2$)$^2$/Hz]')
    plt.title('280')

    plt.subplot(338)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 320)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x, y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD (m/s$^2$)$^2$/Hz]')
    plt.title('320')

    plt.subplot(339)
    f, pxx = psd_welch(acceleration_filtered_no_grav[0:450], fs, 360)
    plt.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    print(x)
    plt.scatter(x, y)
    plt.axvline(x=x)
    plt.xlabel('HZ')
    plt.ylabel('PSD (m/s$^2$)$^2$/Hz]')
    plt.title('360')
    plt.tight_layout()
    plt.savefig('welch_windows_8hz.png')

    plt.show()


def test_welch_wrist_data():
    """Test welch method of PSD estimation visually on data when wearing device

    :return: Plots
    """

    from process_data import remove_gravity_ENMO, \
        calculate_magnitude_acceleration, \
        butter_lowpass_IIR_filter, integrate_time_series, gs_to_accel, \
        psd_welch, is_tremor
    from package_data import extrapolate_accel_data_testing

    import numpy as np
    import matplotlib.pyplot as plt

    fs = 123
    x_accel, y_accel, z_accel = extrapolate_accel_data_testing('wrist_data.txt')

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

    # plot filtered acceleration without gravity
    f1 = plt.figure()
    ax1 = f1.add_subplot(311)
    ax1.plot(time[0:1000], acceleration_filtered_no_grav[0:1000], color='g')
    plt.xlabel('time (s)')
    plt.ylabel('acceleration (m/s^2)')
    plt.title('Filtered Wrist Data')
    plt.savefig('filtered_wrist_data.png')

    f, pxx = psd_welch(acceleration_filtered_no_grav[0:500], fs)

    # test if tremor present in segment
    alert = is_tremor(f, pxx)

    ax2 = f1.add_subplot(312)
    ax2.semilogy(f, pxx, color='r')
    plt.xlabel('Frequency (HZ)')
    plt.ylabel('PSD (m/s$^2$)$^2$/Hz]')
    plt.title('First Half of PSD of Wrist Data Segment Tremor : %r' % (alert))


    f, pxx = psd_welch(acceleration_filtered_no_grav[500:1000], fs)

    # test if tremor present in segment
    alert = is_tremor(f, pxx)

    ax3 = f1.add_subplot(313)
    ax3.semilogy(f, pxx, color='r')
    plt.xlabel('Frequency (HZ)')
    plt.ylabel('PSD (m/s$^2$)$^2$/Hz]')
    plt.title('Second Half of PSD of Wrist Data Segment Tremor : %r' %(alert))
    f1.savefig('2hz_PSD.png')
    plt.tight_layout()
    plt.savefig('wrist_data_with_tremor.png')
    plt.show()


def display_acceleration(frame, f, a):
    """Display the magnitude of acceleration inside embedded tkinter graph

    :param f: Parent GUI Figure
    :param a: Parent GUI axis
    :return:
    """
    from data_analysis.process_data import butter_lowpass_IIR_filter, calculate_magnitude_acceleration, remove_gravity_ENMO, gs_to_accel
    from data_analysis.package_data import get_data
    import numpy as np

    f.canvas.draw()
    a.clear()

    fs = 100
    x_accel, y_accel, z_accel = get_data('data_rate_test.txt')

    # remove high frequencies
    x_filt = butter_lowpass_IIR_filter(x_accel, 14, 100)
    y_filt = butter_lowpass_IIR_filter(y_accel, 14, 100)
    z_filt = butter_lowpass_IIR_filter(z_accel, 14, 100)
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


    # plot filtered acceleration without gravity
    frame.line = a.plot(time, acceleration_filtered_no_grav, color='c', label='Acceleration')
    a.set_xlabel('Time (s)')
    a.set_ylabel('Acceleration - Gravity Compensated (m/s$^2$)')
    a.set_title(r'Magnitude of Acceleration')
    a.legend()
    a.grid(which='major', linestyle='--', color='grey')


def display_displacement(frame, f, a):
    """Displays displacement vector of given tremor

    :param frame: Parent GUI frame window where the graph is displayed
    :param f: Parent GUI figure
    :param a: Parent GUI axes
    :return:
    """

    from data_analysis.process_data import get_disp_amplitude, butter_lowpass_IIR_filter, remove_gravity_ENMO

    from data_analysis.process_data import butter_lowpass_IIR_filter, calculate_magnitude_acceleration, \
        remove_gravity_ENMO, gs_to_accel
    from data_analysis.package_data import get_data
    import numpy as np
    import matplotlib.pyplot as plt

    f.canvas.draw()
    a.clear()

    highcut = 14
    lowcut = 1
    fs = 100
    x_accel, y_accel, z_accel = get_data('data_rate_test.txt')

    # remove high frequencies
    x_filt = butter_lowpass_IIR_filter(x_accel, highcut, fs)
    y_filt = butter_lowpass_IIR_filter(y_accel, highcut, fs)
    z_filt = butter_lowpass_IIR_filter(z_accel, highcut, fs)
    time = np.arange(0, len(x_filt), 1) / float(fs)

    # calculate enmo
    enmo = np.array(remove_gravity_ENMO(x_filt, y_filt, z_filt))

    # get displacement and envelope
    mean_disp, disp, envelope = get_disp_amplitude(enmo, lowcut, fs)

    # plot on GUI
    frame.line = a.plot(time, disp, label='Displacement', color='c')
    a.plot(time, envelope, label='Envelope', linestyle='dashed', color='r')
    a.set_xlabel('Time (s)')
    a.set_ylabel('Displacement (mm)')
    a.set_title('Displacement vs Time (w/ Envelope): Mean = %.2f mm' %(mean_disp),)
    a.grid(False)
    a.legend()


def display_psd(frame, f, a1, a2, a3, a4, a5, a6, a7, a8):
    """Display 4 windows of welch calculated PSD in GUI

    :param frame:
    :param f: figure
    :param a1: axis 1
    :param a2: axis 2
    :param a3: axis 3
    :param a4: axis 4
    :param a5: axis 5
    :param a6: axis 6
    :param a7: axis 7
    :param a8: axis 8
    :return:
    """
    from data_analysis.process_data import butter_lowpass_IIR_filter, calculate_magnitude_acceleration, \
        remove_gravity_ENMO, gs_to_accel, psd_welch, is_tremor
    from data_analysis.package_data import get_windows
    import numpy as np
    import matplotlib.pyplot as plt

    f.canvas.draw()
    a1.clear()
    a1.grid(which='major', linestyle='--', color='grey')
    a2.clear()
    a2.grid(which='major', linestyle='--', color='grey')
    a3.clear()
    a3.grid(which='major', linestyle='--', color='grey')
    a4.clear()
    a4.grid(which='major', linestyle='--', color='grey')
    a5.clear()
    a5.grid(which='major', linestyle='--', color='grey')
    a6.clear()
    a6.grid(which='major', linestyle='--', color='grey')
    a7.clear()
    a7.grid(which='major', linestyle='--', color='grey')
    a8.clear()
    a8.grid(which='major', linestyle='--', color='grey')

    highcut = 14
    fs = 100

    x_wins, y_wins, z_wins = get_windows('data_rate_test.txt', 4)

# WINDOW 1
    # remove high frequencies
    x_filt_w1 = butter_lowpass_IIR_filter(x_wins[0], highcut, fs)
    y_filt_w1 = butter_lowpass_IIR_filter(y_wins[0], highcut, fs)
    z_filt_w1 = butter_lowpass_IIR_filter(z_wins[0], highcut, fs)
    time = np.arange(0, len(x_filt_w1), 1) / float(fs)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_rawg_1 = calculate_magnitude_acceleration(x_filt_w1, y_filt_w1, z_filt_w1)
    acceleration_raw_no_gravg_1 = remove_gravity_ENMO(x_filt_w1, y_filt_w1, z_filt_w1)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filteredg_1 = calculate_magnitude_acceleration(x_filt_w1, y_filt_w1, z_filt_w1)
    acceleration_filtered_no_gravg_1 = remove_gravity_ENMO(x_filt_w1, y_filt_w1, z_filt_w1)

    # remove gravity
    acceleration_filtered_no_grav_1 = gs_to_accel(acceleration_filtered_no_gravg_1)

    # plot filtered acceleration without gravity
    a1.plot(time, acceleration_filtered_no_grav_1, color='c', label='Acceleration')
    a1.set_xlabel('time (s)')
    a1.set_ylabel('acceleration (m/s^2)')
    a1.set_xticks([0,1,2,3,4])
    a1.legend()

    # calculate psd of window
    f_1, pxx_1 = psd_welch(acceleration_filtered_no_grav_1, fs)

    alert, DF = is_tremor(f_1, pxx_1)

    a5.semilogy(f_1, pxx_1, color='r', label='PSD')
    a5.set_title('DF = %.1f Hz | Tremor: %r' %(DF, alert))
    a5.set_xlabel('Frequency (Hz)')
    a5.legend()

# WINDOW 2
    # remove high frequencies
    x_filt_w2 = butter_lowpass_IIR_filter(x_wins[1], highcut, fs)
    y_filt_w2 = butter_lowpass_IIR_filter(y_wins[1], highcut, fs)
    z_filt_w2 = butter_lowpass_IIR_filter(z_wins[1], highcut, fs)
    time = np.arange(0, len(x_filt_w2), 1) / float(fs)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_rawg_2 = calculate_magnitude_acceleration(x_filt_w2, y_filt_w2, z_filt_w2)
    acceleration_raw_no_gravg_2 = remove_gravity_ENMO(x_filt_w2, y_filt_w2, z_filt_w2)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filteredg_2 = calculate_magnitude_acceleration(x_filt_w2, y_filt_w2, z_filt_w2)
    acceleration_filtered_no_gravg_2 = remove_gravity_ENMO(x_filt_w2, y_filt_w2, z_filt_w2)

    # remove gravity
    acceleration_filtered_no_grav_2 = gs_to_accel(acceleration_filtered_no_gravg_2)

    # plot filtered acceleration without gravity
    a2.plot(time, acceleration_filtered_no_grav_2, color='c')
    a2.set_xlabel('time (s)')
    a2.set_ylabel('acceleration (m/s^2)')
    a2.set_xticks([0,1,2,3,4])
    a2.set_xticklabels(['4','5','6','7','8'])

    # calculate psd of window
    f_2, pxx_2 = psd_welch(acceleration_filtered_no_grav_2, fs)

    alert, DF = is_tremor(f_2, pxx_2)

    a6.semilogy(f_2, pxx_2, color='r')
    a6.set_title('DF = %.1f Hz | Tremor: %r' %(DF, alert))
    a6.set_xlabel('Frequency (Hz)')


# WINDOW 3
    # remove high frequencies
    x_filt_w3 = butter_lowpass_IIR_filter(x_wins[2], highcut, fs)
    y_filt_w3 = butter_lowpass_IIR_filter(y_wins[2], highcut, fs)
    z_filt_w3 = butter_lowpass_IIR_filter(z_wins[2], highcut, fs)
    time = np.arange(0, len(x_filt_w3), 1) / float(fs)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_rawg_3 = calculate_magnitude_acceleration(x_filt_w3, y_filt_w3, z_filt_w3)
    acceleration_raw_no_gravg_3 = remove_gravity_ENMO(x_filt_w3, y_filt_w3, z_filt_w3)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filteredg_3 = calculate_magnitude_acceleration(x_filt_w3, y_filt_w3, z_filt_w3)
    acceleration_filtered_no_gravg_3 = remove_gravity_ENMO(x_filt_w3, y_filt_w3, z_filt_w3)

    # remove gravity
    acceleration_filtered_no_grav_3 = gs_to_accel(acceleration_filtered_no_gravg_3)

    # plot filtered acceleration without gravity
    a3.plot(time, acceleration_filtered_no_grav_3, color='c')
    a3.set_xlabel('time (s)')
    a3.set_ylabel('acceleration (m/s^2)')
    a3.set_xticks([0,1,2,3,4])
    a3.set_xticklabels(['8', '9', '10', '11', '12'])

    # calculate psd of window
    f_3, pxx_3 = psd_welch(acceleration_filtered_no_gravg_3, fs)
    alert, DF = is_tremor(f_3, pxx_3)

    a7.semilogy(f_3, pxx_3, color='r')
    a7.set_title('DF = %.1f Hz | Tremor: %r' %(DF, alert))
    a7.set_xlabel('Frequency (Hz)')


# WINDOW 4
    # WINDOW 3
    # remove high frequencies
    x_filt_w4 = butter_lowpass_IIR_filter(x_wins[3], highcut, fs)
    y_filt_w4 = butter_lowpass_IIR_filter(y_wins[3], highcut, fs)
    z_filt_w4 = butter_lowpass_IIR_filter(z_wins[3], highcut, fs)
    time = np.arange(0, len(x_filt_w4), 1) / float(fs)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_rawg_4 = calculate_magnitude_acceleration(x_filt_w4, y_filt_w4, z_filt_w4)
    acceleration_raw_no_gravg_4 = remove_gravity_ENMO(x_filt_w4, y_filt_w4, z_filt_w4)

    # calculate magnitude of acceleration with and without grav (filtered)
    acceleration_filteredg_4 = calculate_magnitude_acceleration(x_filt_w4, y_filt_w4, z_filt_w4)
    acceleration_filtered_no_gravg_4 = remove_gravity_ENMO(x_filt_w4, y_filt_w4, z_filt_w4)

    # remove gravity
    acceleration_filtered_no_grav_4 = gs_to_accel(acceleration_filtered_no_gravg_4)

    # plot filtered acceleration without gravity
    a4.plot(time, acceleration_filtered_no_grav_4, color='c')
    a4.set_xlabel('time (s)')
    a4.set_ylabel('acceleration (m/s^2)')
    a4.set_xticks([0,1,2,3,4])
    a4.set_xticklabels(['12', '13', '14', '15', '16'])

    # calculate psd of window
    f_4, pxx_4 = psd_welch(acceleration_filtered_no_gravg_4, fs)
    alert, DF = is_tremor(f_4, pxx_4)

    a8.semilogy(f_4, pxx_4, color='r')
    a8.set_title('DF= %.1f Hz | Tremor: %r' %(DF, alert))
    a8.set_xlabel('Frequency (Hz)')
    f.tight_layout()


def generate_noisy_sin(freq):
    """Generate noisy sinusoid corrupted by 0.001 V**2/Hz
    of white noise sampled at given frequency

    :param freq: frequency of sinusoid to make
    :return:
    """
    import numpy as np
    time_len = 16
    fs = 100

    time = np.linspace(0, 16, fs*16)
    noise_power = 0.001 * fs /2
    y = 0.1*np.sin(2*np.pi*freq*time)
    y += np.random.normal(scale=np.sqrt(noise_power), size=time.shape)

    return time, y


def test_welch_params(data, nperseg, noverlap):
    """Test effects of window size and overlap size on
    Welch accuracy

    :param data: data segment to perform test on
    :param nperseg: number of points in window to test (np.array)
    :param noverlap: number of points to overlap to test (np.array)
    :return: plots
    """
    import matplotlib.pyplot as plt
    from data_analysis.process_data import psd_welch_test, get_DF
    plt.rcParams['toolbar'] = 'None'
    fig = plt.figure(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')
    j = 0
    time = len(data) / 100.0
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    f, pxx = psd_welch_test(data, 100, nperseg, noverlap)
    ax.semilogy(f, pxx)
    x, y = get_DF(f, pxx)
    ax.scatter(x,y)
    plt.title('DF: %.1f Hz \n noverlap = %d|nperseg = %d' % (x, noverlap, nperseg))
    plt.show()


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    time, y = generate_noisy_sin(8)
    import numpy as np

    half_sec = y[0:50]
    one_and_half_sec = y[0:150]
    two_sec = y[0:200]
    two_and_half_sec = y[0:250]
    three_sec = y[0:300]
    three_and_half_sec = y[0:350]
    four_sec = y[0:400]


    test_welch_params(four_sec, 150, 75)











