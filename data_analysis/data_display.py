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


def display_displacement(frame, f, a1, a2, a3, a4, a5, a6, a7, a8):
    """Displays displacement vector of given tremor

    :param frame: Parent GUI frame window where the graph is displayed
    :param f: Parent GUI figure
    :param a: Parent GUI axes
    :return:
    """

    from data_analysis.process_data import get_disp_amplitude, butter_lowpass_IIR_filter, remove_gravity_ENMO

    from data_analysis.process_data import butter_lowpass_IIR_filter, calculate_magnitude_acceleration, \
        remove_gravity_ENMO, gs_to_accel, psd_welch, is_tremor
    from data_analysis.package_data import get_data, get_windows
    import numpy as np
    import matplotlib.pyplot as plt

    f.canvas.draw()
    a1.clear()
    a2.clear()
    a3.clear()
    a4.clear()
    a5.clear()
    a6.clear()
    a7.clear()
    a8.clear()

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

    f_1, pxx_1 = psd_welch(acceleration_filtered_no_grav_1, fs)

    alert, DF = is_tremor(f_1, pxx_1)

    mean_disp, disp, envelope = get_disp_amplitude(np.array(acceleration_filtered_no_gravg_1), lowcut, fs)
    a1.plot(np.arange(0,len(acceleration_filtered_no_grav_1),1), acceleration_filtered_no_grav_1, label='Acceleration')
    a1.set_title('Acceleration')
    a1.set_ylabel('m/s$^2$')
    a1.set_xticks([0, 100, 200, 300, 400])
    a1.set_xticklabels(['0','1','2','3','4'])

    a1.legend()
    a5.plot(np.arange(0, len(disp), 1), envelope, color='r', label='Envelope')
    a5.plot(np.arange(0, len(disp), 1), disp, color='g', label='Displacement')
    a5.set_title('Mean: %.2f | Tremor: %r' % (mean_disp, alert))
    a5.set_xlabel('Time (s)')
    a5.set_ylabel('Displacement (mm)')
    a5.set_xticks([0, 100, 200, 300, 400])
    a5.set_xticklabels(['0', '1', '2', '3', '4'])
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

    f_1, pxx_1 = psd_welch(acceleration_filtered_no_grav_2, fs)

    alert, DF = is_tremor(f_1, pxx_1)

    mean_disp, disp, envelope = get_disp_amplitude(np.array(acceleration_filtered_no_gravg_2), lowcut, fs)
    a2.plot(np.arange(0, len(acceleration_filtered_no_grav_2), 1), acceleration_filtered_no_grav_2,
            label='Acceleration')
    a2.set_title('Acceleration')
    a2.set_xticks([0, 100, 200, 300, 400])
    a2.set_xticklabels(['4', '5', '6', '7', '8'])
    a6.plot(np.arange(0, len(disp), 1), envelope, color='r', label='Envelope')
    a6.plot(np.arange(0, len(disp), 1), disp, color='g', label='Displacement')
    a6.set_title('Mean: %.2f | Tremor: %r' % (mean_disp, alert))
    a6.set_xlabel('Time (s)')
    a6.set_ylabel('Displacement (mm)')
    a6.set_xticks([0, 100, 200, 300, 400])
    a6.set_xticklabels(['4', '5', '6', '7', '8'])

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

    f_1, pxx_1 = psd_welch(acceleration_filtered_no_grav_3, fs)

    alert, DF = is_tremor(f_1, pxx_1)

    mean_disp, disp, envelope = get_disp_amplitude(np.array(acceleration_filtered_no_gravg_3), lowcut, fs)
    a3.plot(np.arange(0, len(acceleration_filtered_no_grav_1), 1), acceleration_filtered_no_grav_3,
            label='Acceleration')
    a3.set_title('Acceleration')
    a3.set_xticks([0, 100, 200, 300, 400])
    a3.set_xticklabels(['8', '9', '10', '11', '12'])
    a7.plot(np.arange(0, len(disp), 1), envelope, color='r', label='Envelope')
    a7.plot(np.arange(0, len(disp), 1), disp, color='g', label='Displacement')
    a7.set_title('Mean: %.2f | Tremor: %r' % (mean_disp, alert))
    a7.set_xlabel('Time (s)')
    a7.set_ylabel('Displacement (mm)')
    a7.set_xticks([0, 100, 200, 300, 400])
    a7.set_xticklabels(['8', '9', '10', '11', '12'])

    # WINDOW 4
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

    f_4, pxx_4 = psd_welch(acceleration_filtered_no_gravg_4, fs)
    alert, DF = is_tremor(f_4, pxx_4)

    mean_disp, disp, envelope = get_disp_amplitude(np.array(acceleration_filtered_no_gravg_4), lowcut, fs)
    a4.plot(np.arange(0, len(acceleration_filtered_no_grav_1), 1), acceleration_filtered_no_grav_4,
            label='Acceleration')
    a4.set_title('Acceleration')
    a4.set_xticks([0, 100, 200, 300, 400])
    a4.set_xticklabels(['12', '13', '14', '15', '16'])
    a8.plot(np.arange(0, len(disp), 1), envelope, color='r', label='Envelope')
    a8.plot(np.arange(0, len(disp), 1), disp, color='g', label='Displacement')
    a8.set_title('Mean: %.2f | Tremor: %r' % (mean_disp, alert))
    a8.set_xlabel('Time (s)')
    a8.set_ylabel('Displacement (mm)')
    a8.set_xticks([0, 100, 200, 300, 400])
    a8.set_xticklabels(['12', '13', '14', '15', '16'])

    f.tight_layout()


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

    a5.semilogy(f_1, pxx_1, color='r', label='Power Spectral Density')
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


def get_stats():
    from data_analysis.package_data import get_windows
    from data_analysis.process_data import butter_lowpass_IIR_filter, get_disp_amplitude, is_tremor, remove_gravity_ENMO, psd_welch, get_disp_quant,  describe_tremor_freq
    import numpy as np
    x_wins, y_wins, z_wins = get_windows('data_rate_test.txt', 4)

    highcut = 14
    lowcut = 1
    fs = 100

    mean_disp_wins = []
    is_tremor_wins = []
    df_wins = []

    for i in range(len(x_wins)):
        xfilt = butter_lowpass_IIR_filter(x_wins[i], highcut, fs)
        yfilt = butter_lowpass_IIR_filter(y_wins[i], highcut, fs)
        zfilt = butter_lowpass_IIR_filter(z_wins[i], highcut, fs)

        enmofilt = np.array(remove_gravity_ENMO(xfilt, yfilt, zfilt))

        mean_disp, disp, env = get_disp_amplitude(enmofilt, lowcut, fs)

        mean_disp_wins.append(mean_disp)

        freqs, pxx = psd_welch(enmofilt, fs)
        is_trem, df = is_tremor(freqs, pxx)

        is_tremor_wins.append(is_trem)
        df_wins.append(df)


    actual_disps = []
    for i in range(len(mean_disp_wins)):
        if is_tremor_wins[i]:
            actual_disps.append(mean_disp_wins[i])

    disp_quant = get_disp_quant(np.mean(actual_disps))
    pd, et = describe_tremor_freq(np.mean(df_wins))

    return mean_disp_wins, is_tremor_wins, df_wins, disp_quant, pd, et
