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


def calc_amplitude(data):
    """Get the amplitude of a tremor peak
    :param data: array of data (np.array) containing a single peak
    :return: amplitude of peak
    """


def is_tremor(frequency, amplitude, data):
    """Determine if data signal constitutes a tremor
    :param frequency: frequency (float) of tremor (Hz)
    :param amplitude: amplitude (float) of tremor
    :param data: array of data (np.array) containing single peak
    :return:
    """


def psd_welch(data):
    """Estimate power spectral density using Welch’s method.
    Welch’s method [R145] computes an estimate of the power spectral density by dividing the data into overlapping
    segments, computing a modified periodogram for each segment and averaging the periodograms.
    :param data:
    :return:
    """
    import numpy as np
    import scipy


def integrate_time_series(data, fs):
    """Integrate time series data with given frequency

    :param data:
    :param fs:
    :return:
    """
    from scipy import integrate

    x = np.array(range(0, len(data)))

    y = integrate.cumtrapz(data, x=None, dx=1/fs, axis=-1, initial=0)

    return y


def gs_to_accel(data):
    """ Convert to m/s^2

    :param data:
    :return: data in m/s^2
    """


    return data / 9.8


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


def remove_gravity_ENMO(accel_x, accel_y, accel_z):
    """ Remove gravity from signal using the euclidean norm - 1
    See Hees et. al

    :param accel_x: acceleration x vector (m/s^2)
    :param accel_y: acceleration y vector (m/s^2)
    :param accel_z: acceleration z vector (m/s^2)
    :return: magnitude of acceleration w/o DC component (gravity)
    """
    import numpy as np

    vector = np.array([accel_x, accel_y, accel_z])

    normedA_0 = np.array([(np.linalg.norm(v) - 1) for v in vector])

    return np.linalg.norm(vector) - 1


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
    then calculate eudlidean norm -1

    :param accel_x: acceleration x vector (m/s^2)
    :param accel_y: acceleration y vector (m/s^2)
    :param accel_z: acceleration z vector (m/s^2)
    :return: magnitude of acceleration w/o DC component (gravity)
    """


# change to high pass wc = 0.2 Hz
def butter_bandpass(lowcut, highcut, fs, order=5):
    """ Get coefficients for Butterworth bandpass filter.
    Use with butter_bandpass_filter

    :param lowcut: lower cutoff frequency (Hz)
    :param highcut: upper cutoff frequency (Hz)
    :param fs: sampling frequency (Hz)
    :param order: filter order
    :return: Butterworth bandpass filter coefficients
    """
    from scipy.signal import butter
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    """ Filter data using parameters

    :param data: data to apply filter to
    :param lowcut: lower cutoff frequency (Hz)
    :param highcut: uppper cutoff frequency (Hz)
    :param fs: sampling frequency (Hz)
    :param order: filter order
    :return:
    """
    from scipy.signal import lfilter
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


if __name__ == "__main__":
    import numpy as np
    from scipy.signal import freqz
    import matplotlib.pyplot as plt
#
#     N = 400  # signal length of number
#     x = np.arange(0, N, 1)  # generate the time ticks
#     Sines = [np.sin(x * n) * (1 - n) for n in [.9, .75, .5, .25, .12, .03, 0.025]]  # different frequency components
#     y = np.sum(Sines, axis=0)  # add them by column, low frequencies have higher amplitudes
#
#     Low_cutoff, High_cutoff, F_sample = 5, 30, 500
#     Spectrum, Filtered_spectrum, Filtered_signal, Low_point, High_point = bandpass_ifft(y, Low_cutoff, High_cutoff, F_sample)
#
# # **** test filtering raw data ****
#     # plot raw data
#     fig0 = plt.figure()
#     plt.plot(x, y)
#     plt.title("Raw Data")
#
#     # plot high filtered data
#     fig1 = plt.figure()
#     plt.plot(x, Filtered_signal)
#     plt.title("Filtered Data")
#     plt.show()
#
# # ****  test converting gs to m/s^2 ****
#     a = np.array([9.8, 1, 5, 6, 7])
#     removed_gravity = gs_to_accel(a)
#     print(removed_gravity)
#
# # ***** test removing gravity with euclidean norm ****
#     mag = remove_gravity_ENMO(1,1,1)
#     print(mag)
#
# # **** test method of filter to remove gravity ****
#     # Sample rate and desired cutoff frequencies (in Hz).
#     fs = 5000.0
#     lowcut = 500.0
#     highcut = 1250.0
#
#     # Plot the frequency response for a few different orders.
#     plt.figure(1)
#     plt.clf()
#     for order in [3, 6, 9]:
#         b, a = butter_bandpass(lowcut, highcut, fs, order=order)
#         w, h = freqz(b, a, worN=2000)
#         plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = %d" % order)
#
#     plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)],
#              '--', label='sqrt(0.5)')
#     plt.xlabel('Frequency (Hz)')
#     plt.ylabel('Gain')
#     plt.grid(True)
#     plt.legend(loc='best')
#
#     # Filter a noisy signal.
#     T = 0.05
#     nsamples = T * fs
#     t = np.linspace(0, T, nsamples, endpoint=False)
#     a = 0.02
#     f0 = 600.0
#     x = 0.1 * np.sin(2 * np.pi * 1.2 * np.sqrt(t))
#     x += 0.01 * np.cos(2 * np.pi * 312 * t + 0.1)
#     x += a * np.cos(2 * np.pi * f0 * t + .11)
#     x += 0.03 * np.cos(2 * np.pi * 2000 * t)
#     plt.figure(2)
#     plt.clf()
#     plt.plot(t, x, label='Noisy signal')
#
#     y = butter_bandpass_filter(x, lowcut, highcut, fs, order=6)
#     plt.plot(t, y, label='Filtered signal (%g Hz)' % f0)
#     plt.xlabel('time (seconds)')
#     plt.hlines([-a, a], 0, T, linestyles='--')
#     plt.grid(True)
#     plt.axis('tight')
#     plt.legend(loc='upper left')
#
#     plt.show()


    pass
