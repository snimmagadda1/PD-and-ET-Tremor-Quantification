from matplotlib import style
style.use("ggplot")

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
    lowcut = 2
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
    f_3, pxx_3 = psd_welch(acceleration_filtered_no_grav_3, fs)
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
    f_4, pxx_4 = psd_welch(acceleration_filtered_no_grav_4, fs)
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
    lowcut = 2
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

        freqs, pxx = psd_welch(enmofilt*9.8, fs)
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


def poster_graphs_acceleration_displacement():
    from data_analysis.process_data import butter_lowpass_IIR_filter, \
        remove_gravity_ENMO, gs_to_accel, get_disp_amplitude, is_tremor, psd_welch
    import numpy as np
    import matplotlib.pyplot as plt

    x_trem = []
    y_trem = []
    z_trem = []
    x_still = []
    y_still = []
    z_still = []

    fc = 14
    fs = 100
    with open("on_wrist_simulated_tremor1.txt", "r") as f1:
        for line in f1:
            curr_reading = line.split(",")
            x_trem.append(float(curr_reading[0]))
            y_trem.append(float(curr_reading[1]))
            z_trem.append(float(curr_reading[2]))


    with open("arm_extended_no_tremor.txt", "r") as f2:
        for line in f2:
            curr_reading = line.split(",")
            x_still.append(float(curr_reading[0]))
            y_still.append(float(curr_reading[1]))
            z_still.append(float(curr_reading[2]))

    # filter raw accel
    x_filt_trem = butter_lowpass_IIR_filter(x_trem, fc, fs)
    y_filt_trem = butter_lowpass_IIR_filter(y_trem, fc, fs)
    z_filt_trem = butter_lowpass_IIR_filter(z_trem, fc, fs)

    x_filt_still = butter_lowpass_IIR_filter(x_still, fc, fs)
    y_filt_still = butter_lowpass_IIR_filter(y_still, fc, fs)
    z_filt_still = butter_lowpass_IIR_filter(z_still, fc, fs)
    time_trem = np.arange(0, len(x_filt_trem), 1) / float(fs)
    time_still = np.arange(0, len(x_filt_still), 1) / float(fs)

    # remove gravity and convert to gs
    acceleration_filtered_no_gravg_trem = remove_gravity_ENMO(x_filt_trem, y_filt_trem, z_filt_trem)
    acceleration_tremor = gs_to_accel(acceleration_filtered_no_gravg_trem)

    acceleration_filtered_no_gravg_still = remove_gravity_ENMO(x_filt_still, y_filt_still, z_filt_still)
    acceleration_still = gs_to_accel(acceleration_filtered_no_gravg_still)


    # get displacement and envelope
    mean_disp_trem, disp_trem, envelope_trem = get_disp_amplitude(np.array(acceleration_filtered_no_gravg_trem), 2, 14)
    mean_disp_still, disp_still, envelope_still = get_disp_amplitude(np.array(acceleration_filtered_no_gravg_still), 2, 14)

    f = plt.figure(figsize=(16, 10))
    ax1 = f.add_subplot(321)
    ax2 = f.add_subplot(322, sharey=ax1)
    ax3 = f.add_subplot(323)
    ax4 = f.add_subplot(324, sharey=ax3)
    ax5 = f.add_subplot(325)
    ax6 = f.add_subplot(326)

    #plot accelerations
    ax1.plot(time_trem[500:900], acceleration_tremor[500:900], c='b')
    ax1.set_xticks([5, 6, 7, 8, 9])
    ax1.set_xticklabels(['0', '1', '2', '3', '4'])
    ax1.set_title("Arm Extended: Tremor", fontsize=24)
    ax1.set_ylim([-14,14])
    ax1.set_ylabel("Acceleration (m/s)", fontsize=18)

    ax2.plot(time_still[500:900], acceleration_still[500:900], c='b')
    ax2.set_xticks([5, 6, 7, 8, 9])
    ax2.set_xticklabels(['0', '1', '2', '3', '4'])
    ax2.set_title("Arm Extended: No Tremor", fontsize=24)
    ax2.set_ylim([-14,14])

    # plot displacements
    ax3.plot(time_trem[500:900], disp_trem[500:900], color='g', label='Displacement')
    ax3.plot(time_trem[500:900], envelope_trem[500:900], color='r', label='Envelope')
    ax3.set_xticks([5, 6, 7, 8, 9])
    ax3.set_title("Calculated Displacement", fontsize=24)
    ax3.set_yticks([-3, -1.5, 0, 1.5, 3])
    ax3.set_xticklabels(['0', '1', '2', '3', '4'])
    ax3.set_ylim([-3,3])
    ax3.set_ylabel("Displacement (mm)", fontsize=18)
    ax3.legend(loc='upper left')

    ax4.plot(time_still[500:900], disp_still[500:900], color='g')
    ax4.plot(time_still[500:900], envelope_still[500:900], color='r')
    ax4.set_title("Calculated Displacement", fontsize=18)
    ax4.set_xticks([5, 6, 7, 8, 9])
    ax4.set_yticks([-3, -1.5, 0, 1.5, 3])
    ax4.set_xticklabels(['0', '1', '2', '3', '4'])
    ax4.set_ylim([-3, 3])

    f_trem, pxx_trem = psd_welch(acceleration_tremor, fs)

    alert_trem, DF_trem = is_tremor(f_trem, pxx_trem)

    ax5.semilogy(f_trem, pxx_trem, color='r', label='Power Spectral Density')
    ax5.set_title('DF = %.2f Hz Tremor: %r' % (DF_trem, alert_trem), fontsize=24)
    ax5.set_xlabel('Frequency (Hz)', fontsize=16)
    ax5.set_ylabel(r'$\frac{(m/s^2)^2}{\sqrt{Hz}}$', fontweight='bold', fontsize=18)
    ax5.set_ylim([0.0001, 100])
    ax5.set_xlim([0, 30])


    f_still, pxx_still = psd_welch(acceleration_still, fs)

    alert_still, DF_still = is_tremor(f_still, pxx_still)

    ax6.semilogy(f_still, pxx_still, color='r', label='Power Spectral Density')
    ax6.set_title('DF = na Tremor: %r' %  alert_still, fontsize=24)
    ax6.set_xlabel('Frequency (Hz)', fontsize=18)
    ax6.set_ylim([0.0001, 100])
    ax6.set_xlim([0, 30])

    plt.tight_layout()
    plt.savefig('windows.pdf', dpi=300)
    plt.show()

    return 0


def plot_filter_response_poster():
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.signal import freqz
    from data_analysis.process_data import butter_lowpass_IIR, butter_highpass_IIR_filter

    plt.figure(figsize=(12,5))
    plt.clf()

    fc = 14
    fs = 100
    linewidth = 1
    for order in [3, 5, 7]:
        if order == 5:
            linewidth = 3
        b, a = butter_lowpass_IIR(fc, fs, order = order)
        w, h = freqz(b, a, worN=2000)

        plt.plot((fs * 0.5 / np.pi) * w, abs(h), linewidth=linewidth, label="Order = %d" % order)
        linewidth=1

    plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)],'--', label=r'$\sqrt{\frac{1}{2}}$')
    plt.xlabel('Frequency (Hz)', fontsize=18)
    plt.ylabel('Gain', fontsize=18)
    plt.title('Frequency Response of Zero-phase IIR Filter', fontsize=24)
    plt.grid(True)
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig('freq_response.pdf', dpi=300)
    plt.show()


def plot_displacement_errors_poster():
    import numpy as np
    import matplotlib.pyplot as plt

    # get data from caroline
    x_freq = np.array([2,2.2,2.4,2.6,2.8,3,3.2,3.4,3.6,3.8,4,4.2,4.4,4.6,4.8,5,5.2,5.4,5.6,5.8,6,6.2,6.4,6.6,6.8,7,7.2,7.4,7.6,7.8,8,8.2,8.4,8.6,8.8,9,9.2,9.4,9.6,9.8,10,10.2,10.4,10.6,10.8,11,11.2,11.4,11.6,11.8,12,12.2,12.4,12.6,12.8,13])
    low_amp=np.array([2,2,2.7,2.7,2.7,2.7,3.3,3.3,3.3,4,4,4,4.3,4.7,4.7,4.7,5.3,5.3,5.3,5.8,6,6,6,6.7,6.7,6.7,7.3,7.3,7.3,7.7,8,8,8.2,8.7,8.7,8.7,9.2,9.3,9.3,9.7,10,10,10.5,10.5,10.7,10.7,10.8,11.2,11.3,11.5,12,12,12,12.4,12.7,12.7])
    med_amp = np.array([2,2,2.7,2.7,2.7,2.7,3.3,3.3,3.3,4,4,4,4.2,4.7,4.7,4.7,5.3,5.3,5.3,5.8,6,6,6,6.7,6.7,6.7,7.3,7.3,7.3,7.5,8,8,8,8.7,8.7,8.7,9.2,9.3,9.3,9.5,10,10,10,10.5,10.7,10.7,11,11.3,11.3,11.7,12,12,12,12.5,12.7,12.7])
    high_amp = np.array([2,2,2.7,2.7,2.7,2.7,3.3,3.3,3.3,4,4,4,4,4.7,4.7,4.7,5.3,5.3,5.3,6,6,6,6.3,6.7,6.7,6.7,7.3,7.3,7.3,7.8,8,8,8,8.7,8.7,8.7,9.2,9.3,9.3,9.7,10,10,10,10.7,10.7,10.7,11.2,11.3,11.3,11.5,12,12,12.2,12.7,12.7,12.7])


    low_diff = low_amp - x_freq
    med_diff = med_amp - x_freq
    high_diff = high_amp - x_freq

    print(low_diff.mean())
    print(med_diff.mean())
    print(high_diff.mean())

    f = plt.figure(figsize=(12, 8))
    ax = f.add_subplot(111)
    ax.boxplot([low_diff, med_diff, high_diff])

    plt.show()



def plot_frequency_errors_poster():
    from scipy.stats import f_oneway, stats
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    from statsmodels.stats.multicomp import MultiComparison
    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt

    # caroline data
    x_freq = np.arange(2, 13.2, 0.2)

    # get data from caroline
    low_amp = np.array(
        [2, 2, 2.7, 2.7, 2.7, 2.7, 3.3, 3.3, 3.3, 4, 4, 4, 4.3, 4.7, 4.7, 4.7, 5.3, 5.3, 5.3, 5.8, 6, 6, 6, 6.7, 6.7,
         6.7, 7.3, 7.3, 7.3, 7.7, 8, 8, 8.2, 8.7, 8.7, 8.7, 9.2, 9.3, 9.3, 9.7, 10, 10, 10.5, 10.5, 10.7, 10.7, 10.8,
         11.2, 11.3, 11.5, 12, 12, 12, 12.4, 12.7, 12.7])
    med_amp = np.array(
        [2, 2, 2.7, 2.7, 2.7, 2.7, 3.3, 3.3, 3.3, 4, 4, 4, 4.2, 4.7, 4.7, 4.7, 5.3, 5.3, 5.3, 5.8, 6, 6, 6, 6.7, 6.7,
         6.7, 7.3, 7.3, 7.3, 7.5, 8, 8, 8, 8.7, 8.7, 8.7, 9.2, 9.3, 9.3, 9.5, 10, 10, 10, 10.5, 10.7, 10.7, 11, 11.3,
         11.3, 11.7, 12, 12, 12, 12.5, 12.7, 12.7])
    high_amp = np.array(
        [2, 2, 2.7, 2.7, 2.7, 2.7, 3.3, 3.3, 3.3, 4, 4, 4, 4, 4.7, 4.7, 4.7, 5.3, 5.3, 5.3, 6, 6, 6, 6.3, 6.7, 6.7, 6.7,
         7.3, 7.3, 7.3, 7.8, 8, 8, 8, 8.7, 8.7, 8.7, 9.2, 9.3, 9.3, 9.7, 10, 10, 10, 10.7, 10.7, 10.7, 11.2, 11.3, 11.3,
         11.5, 12, 12, 12.2, 12.7, 12.7, 12.7])

    # low = 2-5.8 Hz
    # med = 6-9.8 Hz
    # highs = 10-13 Hz

    low_freq1 = np.array(low_amp[0:18])
    low_freq2 = np.array(med_amp[0:18])
    low_freq3 = np.array(high_amp[0:18])

    med_freq1 = np.array(low_amp[18:36])
    med_freq2 = np.array(med_amp[18:36])
    med_freq3 = np.array(high_amp[18:36])

    high_freq1 = np.array(low_amp[36:54])
    high_freq2 = np.array(med_amp[36:54])
    high_freq3 = np.array(high_amp[36:54])

    x_freq_lows = x_freq[0:18]
    x_freq_meds = x_freq[18:36]
    x_freq_highs = x_freq[36:54]

    diff_low = np.array([])
    diff_med = np.array([])
    diff_high = np.array([])

    for i in [low_freq1, low_freq2, low_freq3]:
        diff1 = i - x_freq_lows
        diff_low = np.append(diff_low, diff1)

    for i in [med_freq1, med_freq2, med_freq3]:
        diff2 = i - x_freq_meds
        diff_med = np.append(diff_med, diff2)

    for i in [high_freq1, high_freq2, high_freq3]:
        diff3 = i - x_freq_highs
        diff_high = np.append(diff_high, diff3)




    f = plt.figure(figsize=(14, 10))
    ax = f.add_subplot(121)
    ax2 = f.add_subplot(122)
    bp = ax.boxplot([diff_low, diff_med, diff_high], patch_artist=True, notch=True)


    # low_amp = np.array(
    #     [2, 2, 2.7, 2.7, 2.7, 2.7, 3.3, 3.3, 3.3, 4, 4, 4, 4.3, 4.7, 4.7, 4.7, 5.3, 5.3, 5.3, 5.8, 6, 6, 6, 6.7, 6.7,
    #      6.7, 7.3, 7.3, 7.3, 7.7, 8, 8, 8.2, 8.7, 8.7, 8.7, 9.2, 9.3, 9.3, 9.7, 10, 10, 10.5, 10.5, 10.7, 10.7, 10.8,
    #      11.2, 11.3, 11.5, 12, 12, 12, 12.4, 12.7, 12.7])
    # med_amp = np.array(
    #     [2, 2, 2.7, 2.7, 2.7, 2.7, 3.3, 3.3, 3.3, 4, 4, 4, 4.2, 4.7, 4.7, 4.7, 5.3, 5.3, 5.3, 5.8, 6, 6, 6, 6.7, 6.7,
    #      6.7, 7.3, 7.3, 7.3, 7.5, 8, 8, 8, 8.7, 8.7, 8.7, 9.2, 9.3, 9.3, 9.5, 10, 10, 10, 10.5, 10.7, 10.7, 11, 11.3,
    #      11.3, 11.7, 12, 12, 12, 12.5, 12.7, 12.7])
    # high_amp = np.array(
    #     [2, 2, 2.7, 2.7, 2.7, 2.7, 3.3, 3.3, 3.3, 4, 4, 4, 4, 4.7, 4.7, 4.7, 5.3, 5.3, 5.3, 6, 6, 6, 6.3, 6.7, 6.7, 6.7,
    #      7.3, 7.3, 7.3, 7.8, 8, 8, 8, 8.7, 8.7, 8.7, 9.2, 9.3, 9.3, 9.7, 10, 10, 10, 10.7, 10.7, 10.7, 11.2, 11.3, 11.3,
    #      11.5, 12, 12, 12.2, 12.7, 12.7, 12.7])

    low_diff = low_amp - x_freq
    med_diff = med_amp - x_freq
    high_diff = high_amp - x_freq

    bp1 = ax2.boxplot([low_diff, med_diff, high_diff], patch_artist=True, notch=True)
    ax.set_xticklabels(['Low Freq.', 'Medium Freq.', 'High Freq'], fontsize='16')
    ax.set_ylabel('Difference (Hz)', fontsize='16')
    ax.set_title('Difference between Expected \nand Measured Frequency', fontsize='24')
    for box in bp['boxes']:
        # change outline color
        box.set(color='#0066cc', linewidth=2)
        # change fill color
        box.set(facecolor='#5DBCD2')

    ## change color and linewidth of the whiskers
    for whisker in bp['whiskers']:
        whisker.set(color='#0066cc', linewidth=2)

    ## change color and linewidth of the caps
    for cap in bp['caps']:
        cap.set(color='#0066cc', linewidth=2)

    ## change color and linewidth of the medians
    for median in bp['medians']:
        median.set(color='#0066cc', linewidth=2)

    ## change the style of fliers and their fill
    for flier in bp['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)

    for box in bp1['boxes']:
        # change outline color
        box.set(color='#0066cc', linewidth=2)
        # change fill color
        box.set(facecolor='#5DBCD2')

        ## change color and linewidth of the whiskers
    for whisker in bp1['whiskers']:
        whisker.set(color='#0066cc', linewidth=2)

        ## change color and linewidth of the caps
    for cap in bp1['caps']:
        cap.set(color='#0066cc', linewidth=2)

        ## change color and linewidth of the medians
    for median in bp1['medians']:
        median.set(color='#0066cc', linewidth=2)

        ## change the style of fliers and their fill
    for flier in bp1['fliers']:
        flier.set(marker='o', color='#e7298a', alpha=0.5)

    ax2.set_xticklabels(['Low Amp.', 'Medium Amp.', 'High Amp.'], fontsize='16')
    ax2.set_ylabel('Difference (Hz)', fontsize='16')
    ax2.set_title('Difference between Expected \nand Measured Frequency', fontsize='24')

    ax.set_ylim([-1,1])
    ax2.set_ylim([-1, 1])
    plt.tight_layout()
    plt.savefig('box_whisker.pdf', dpi=300)
    plt.show()

    # anova on frequencies
    F, p = f_oneway(diff_low, diff_med, diff_high)

    # tukey on frequencies


    print("Pval: " + str(p*2))
    print("Fstat: " + str(F))



if __name__ == "__main__":
    import numpy as np

    plot_frequency_errors_poster()


