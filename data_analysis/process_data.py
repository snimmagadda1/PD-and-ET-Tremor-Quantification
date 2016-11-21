def bandpass_ifft(X, Low_cutoff, High_cutoff, F_sample, M=None):
    """Bandpass filtering on a real signal using inverse FFT

    X: 1-D numpy array of floats, the real time domain signal (time series) to be filtered
    Low_cutoff: float, frequency components below this frequency will not pass the filter (physical frequency in unit of Hz)
    High_cutoff: float, frequency components above this frequency will not pass the filter (physical frequency in unit of Hz)
    F_sample: float, the sampling frequency of the signal (physical frequency in unit of Hz)

    1. The input signal must be real, not imaginary nor complex
    2. The Filtered_signal will have only half of original amplitude. Use abs() to restore.
    3. In Numpy/Scipy, the frequencies goes from 0 to F_sample/2 and then from negative F_sample to 0.

    Inspiration from : http://forrestbao.blogspot.com/

    Noise generally with square of sampling freq

    """
    import scipy, numpy

    if M == None:  # if the number of points for FFT is not specified
        M = X.size  # let M be the length of the time series
    Spectrum = scipy.fft(X, n=M)
    [Low_cutoff, High_cutoff, F_sample] = map(float, [Low_cutoff, High_cutoff, F_sample])

    # Convert cutoff frequencies into points on spectrum
    [Low_point, High_point] = map(lambda F: F / F_sample * M / 2,
                                  [Low_cutoff, High_cutoff])  # the division by 2 is because the spectrum is symmetric

    Filtered_spectrum = [Spectrum[i] if i >= Low_point and i <= High_point else 0.0 for i in range(M)]  # Filtering
    Filtered_signal = scipy.ifft(Filtered_spectrum, n=M)  # Construct filtered signal
    return Spectrum, Filtered_spectrum, Filtered_signal, Low_point, High_point


def remove_nan(data):
    """Remove Nan and empty values from data stream
    :param data: array of data (np.array)
    :return:
    """

    cleaned_list = [x for x in data if str(x) != 'nan']
    return cleaned_list


def get_disp_amplitude(enmofilt, lowcut, fs):
    """Get the average displacement of a subset of raw acceleration data
    :param data: array of filtered acceleration data as ENMO (as numpy array)
    :param lowcut: choice of highpass filter cutoff for removing DC
    :param fs: sampling frequency of data in Hz
    :return: average displacement of data in mm
    """

    from scipy.integrate import cumtrapz as integrate
    from scipy.signal import hilbert as envelope
    import numpy as np


    accel = enmofilt*9.8
    accel = accel - np.mean(accel) # recenter about 0
    accel_lowpassed = butter_highpass_IIR_filter(accel, lowcut, fs)

    vel = integrate(accel_lowpassed, dx=1/fs, initial=0)
    vel = vel - np.mean(vel) # recenter about 0
    vel_lowpassed = butter_highpass_IIR_filter(vel, lowcut, fs)

    disp = integrate(vel_lowpassed, dx=1/fs, initial=0)
    disp = disp - np.mean(disp) # recenter about 0
    disp = disp*1000 # convert to mm

    # discarding edges for plotting visualization
    for i in range(0, int(len(disp)*.15)):
        disp[i] = 0
    for i in range(int(len(disp)*.85), len(disp)):
        disp[i] = 0

    # Use Hilbert transform to find envelope of displacement, take average value as mean of envelope
    disp_envelope = np.abs(envelope(disp))

    mean_disp = np.mean(disp_envelope[int(len(disp)*.15):int(len(disp)*.85)]) # only consider middle 70% for mean

    return mean_disp, disp, disp_envelope


def psd_welch(data, fs):
    """Estimate PSD using welch method
    :param data:
    :return:
    """
    from scipy import signal

    f, Pxx_den = signal.welch(data, fs, nperseg=150, noverlap=75, return_onesided=True)

    return f, Pxx_den


def psd_welch_test(data, fs, nperseg, noverlap):
    """Estimate PSD using welch method
    :param data:
    :return:
    """
    from scipy import signal

    f, Pxx_den = signal.welch(data, fs, nperseg=nperseg, noverlap=noverlap, return_onesided=True)

    return f, Pxx_den


def get_DF(f, Pxx_den):
    """Get the dominant frequency (DF) of signal

    :param f: freuqencies (output of psd_welch)
    :param Pxx_den: PSD (output of psd_welch)
    :return: dominant frequency and amplitude
    """
    import numpy as np
    max_y = max(Pxx_den)
    DF = f[np.where(Pxx_den == max_y)]  # Find the x value corresponding to the maximum y value

    return DF, max_y


def integrate_time_series(time, data, fs):
    """Integrate time series data with given frequency

    :param data: x values (m/s^2 or m/s)
    :param fs: sampling frequency (Hz)
    :return: x_int, y_int, z_int
    """
    from scipy import integrate

    y = integrate.cumtrapz(data, time, initial=data[0])

    return y


def gs_to_accel(data):
    """ Convert to m/s^2

    :param data:
    :return: data in m/s^2
    """
    import numpy as np

    return np.array(data) * 9.8


def gravity_compensate(q, acc):
    """ Quaternion approach to removing gravity

    :param q: the quaternion representing the orientation of a 9DOM MARG sensor array
    :param acc: the readings coming from an accelerometer expressed in g
    :return: 3d vector representing dynamic acceleration expressed in g
    """
    g = [0.0, 0.0, 0.0]

    # get expected direction of gravity
    g[0] = 2 * (q[1] * q[3] - q[0] * q[2])
    g[1] = 2 * (q[0] * q[1] + q[2] * q[3])
    g[2] = q[0] * q[0] - q[1] * q[1] - q[2] * q[2] + q[3] * q[3]

    # compensate accelerometer readings with the expected direction of gravity
    return [acc[0] - g[0], acc[1] - g[1], acc[2] - g[2]]


def calculate_magnitude_acceleration(accel_x, accel_y, accel_z):
    """ Calculate magnitude of acceleration

       :param accel_x: acceleration x vector (m/s^2)
       :param accel_y: acceleration y vector (m/s^2)
       :param accel_z: acceleration z vector (m/s^2)
       :return: magnitude of acceleration w/o DC component (gravity)
       """
    import numpy as np

    ans = []
    for i in range(len(accel_x)):
        normedA_0 = np.linalg.norm([accel_x[i], accel_y[i], accel_z[i]])
        ans.append(normedA_0)

    return ans


def remove_gravity_ENMO(accel_x, accel_y, accel_z):
    """ Remove gravity from signal using the euclidean norm - 1
    See Hees et. al

    :param accel_x: acceleration x vector (m/s^2)
    :param accel_y: acceleration y vector (m/s^2)
    :param accel_z: acceleration z vector (m/s^2)
    :return: magnitude of acceleration w/o DC component (gravity)
    """
    import numpy as np

    ans = []
    for i in range(len(accel_x)):
        normedA_0 = np.linalg.norm([accel_x[i], accel_y[i], accel_z[i]]) -1
        ans.append(normedA_0)

    return ans


def remove_gravity_HFEN(accel_x, accel_y, accel_z):
    """ Remove gravity from signal using HPF on each raw signal
    then calculate the euclidean norm

    :param accel_x: acceleration x vector (m/s^2)
    :param accel_y: acceleration y vector (m/s^2)
    :param accel_z: acceleration z vector (m/s^2)
    :return: magnitude of acceleration w/o DC component (gravity)
    """


def remove_gravity_HFENplus(accel_x, accel_y, accel_z):
    """ Remove gravity from signal using HPF on each raw signals
    then 4th order Butterworth LPF wc = 0.2 Hz on raw signals,
    then calculate euclidean norm -1

    :param accel_x: acceleration x vector (m/s^2)
    :param accel_y: acceleration y vector (m/s^2)
    :param accel_z: acceleration z vector (m/s^2)
    :return: magnitude of acceleration w/o DC component (gravity)
    """


def butter_lowpass(highcut, fs, order=4):
    """ Get coefficients for Butterworth lowpass filter.
    Use with butter_lowpass_filter

    :param lowcut: lower cutoff frequency (Hz)
    :param highcut: upper cutoff frequency (Hz)
    :param fs: sampling frequency (Hz)
    :param order: filter order
    :return: Butterworth bandpass filter coefficients
    """
    from scipy.signal import butter
    nyq = 0.5 * fs
    high = highcut / nyq
    b, a = butter(order, [high], btype='lowpass')
    return b, a


def butter_lowpass_IIR(highcut, fs, order=4):
    """ Get coefficients for Butterworth lowpass filter.
    Use with butter_lowpass_IIR_filter

    :param highcut: upper cutoff frequency (Hz)
    :param fs: sampling frequency (Hz)
    :param order: filter order
    :return: Butterworth bandpass filter coefficients
    """
    from scipy.signal import iirfilter
    nyq = 0.5 * fs
    high = highcut / nyq
    b, a = iirfilter(order, [high], btype='lowpass', ftype='butter')
    return b, a


def butter_highpass_IIR(lowcut, fs, order=4):
    """ Get coefficients for Butterworth lowpass filter.
    Use with butter_lowpass_IIR_filter

    :param lowcut: lower cutoff frequency (Hz)
    :param fs: sampling frequency (Hz)
    :param order: filter order
    :return: Butterworth bandpass filter coefficients
    """
    from scipy.signal import iirfilter
    nyq = 0.5 * fs
    low = lowcut / nyq
    b, a = iirfilter(order, [low], btype='highpass', ftype='butter')
    return b, a


def butter_lowpass_filter(data, highcut, fs, order=5):
    """ Filter data using parameters

    :param data: data to apply filter to
    :param highcut: uppper cutoff frequency (Hz)
    :param fs: sampling frequency (Hz)
    :param order: filter order
    :return:
    """
    from scipy.signal import filtfilt
    b, a = butter_lowpass(highcut, fs, order=order)
    y = filtfilt(b, a, data, padlen=100, padtype='odd')
    return y


def butter_lowpass_IIR_filter(data, highcut, fs, order=5):
    """ Filter data using parameters. IIR filter

    :param data: data to apply filter to
    :param highcut: uppper cutoff frequency (Hz)
    :param fs: sampling frequency (Hz)
    :param order: filter order
    :return:
    """
    from scipy.signal import filtfilt
    b, a = butter_lowpass_IIR(highcut, fs, order=order)
    y = filtfilt(b, a, data, padlen=100, padtype='odd')
    return y


def butter_highpass_IIR_filter(data, lowcut, fs, order=5):
    """ Filter data using parameters. IIR filter

    :param data: data to apply filter to
    :param highcut: uppper cutoff frequency (Hz)
    :param fs: sampling frequency (Hz)
    :param order: filter order
    :return:
    """
    from scipy.signal import filtfilt
    b, a = butter_highpass_IIR(lowcut, fs, order=order)
    y = filtfilt(b, a, data, padlen=100, padtype='odd')
    return y


def is_tremor(f, Pxx_den):
    """Identify a tremor based on the PSD

    :param f: frequency (output from psd_welch)
    :param Pxx_den: Power spectal density (output from psd_welch)
    :return: boolean classifying whether a tremor occurred and
    the frequency of the tremor **TO DO: amplitude of tremor**
    """
    isTremor = False

    DF, mag = get_DF(f, Pxx_den)

    if DF >= 2.95 and DF <= 12 and mag > 0.01:
        isTremor = True

    return isTremor, DF

def get_disp_quant(mean_disp):
    tremor_high = 15
    scale_high = 10

    if (mean_disp > tremor_high):
        return 10
    else:
        return (mean_disp/tremor_high)*scale_high



def describe_tremor_freq(df):
    """Describe a tremor as a percentage of PD and ET
    characteristics

    :param DF: Dominant frequency of the tremor (result from is_tremor)
    :return: %PD, %ET
    """
    # PD = 3-7 Hz - mean = 5
    # ET = 4-12 Hz - mean = 8
    import numpy as np

    pd_mean = 5
    et_mean = 8

    dist_pd = np.abs(df-pd_mean)
    dist_et = np.abs(df-et_mean)
    dist_tot = dist_pd + dist_et

    percent_pd = 100*(1 - dist_pd/dist_tot)
    percent_et = 100*(1 - dist_et/dist_tot)

    return percent_pd, percent_et


def demonstrate_functions():
    import numpy as np
    from scipy.signal import freqz
    import matplotlib.pyplot as plt

    N = 400  # signal length of number
    x = np.arange(0, N, 1)  # generate the time ticks
    Sines = [np.sin(x * n) * (1 - n) for n in [.9, .75, .5, .25, .12, .03, 0.025]]  # different frequency components
    y = np.sum(Sines, axis=0)  # add them by column, low frequencies have higher amplitudes

    Low_cutoff, High_cutoff, F_sample = 5, 30, 500
    Spectrum, Filtered_spectrum, Filtered_signal, Low_point, High_point = bandpass_ifft(y, Low_cutoff, High_cutoff,
                                                                                        F_sample)

    # **** test filtering raw data ****
    # plot raw data
    fig0 = plt.figure()
    plt.plot(x, y)
    plt.title("Raw Data")

    # plot high filtered data
    fig1 = plt.figure()
    plt.plot(x, Filtered_signal)
    plt.title("Filtered Data")
    plt.show()

    # ****  test converting gs to m/s^2 ****
    a = np.array([9.8, 1, 5, 6, 7])
    removed_gravity = gs_to_accel(a)
    print(removed_gravity)

    # **** test method of filter to remove gravity ****
    # Sample rate and desired cutoff frequencies (in Hz).
    fs = 5000.0
    lowcut = 500.0
    highcut = 1250.0

    # Plot the frequency response for a few different orders.
    plt.figure(1)
    plt.clf()
    for order in [3, 6, 9]:
        b, a = butter_bandpass(lowcut, highcut, fs, order=order)
        w, h = freqz(b, a, worN=2000)
        plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = %d" % order)

    plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)],
             '--', label='sqrt(0.5)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain')
    plt.grid(True)
    plt.legend(loc='best')

    # Filter a noisy signal.
    T = 0.05
    nsamples = T * fs
    t = np.linspace(0, T, nsamples, endpoint=False)
    a = 0.02
    f0 = 600.0
    x = 0.1 * np.sin(2 * np.pi * 1.2 * np.sqrt(t))
    x += 0.01 * np.cos(2 * np.pi * 312 * t + 0.1)
    x += a * np.cos(2 * np.pi * f0 * t + .11)
    x += 0.03 * np.cos(2 * np.pi * 2000 * t)
    plt.figure(2)
    plt.clf()
    plt.plot(t, x, label='Noisy signal')

    y = butter_bandpass_filter(x, lowcut, highcut, fs, order=6)
    plt.plot(t, y, label='Filtered signal (%g Hz)' % f0)
    plt.xlabel('time (seconds)')
    plt.hlines([-a, a], 0, T, linestyles='--')
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='upper left')

    plt.show()


if __name__ == "__main__":

    pass
