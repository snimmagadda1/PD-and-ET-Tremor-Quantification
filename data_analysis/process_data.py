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
    """
    Remove Nan and empty values from data stream
    :param data: array of data (np.array)
    :return:
    """

    pass


def calc_amplitude(data):
    """
    Get the amplitude of a peak
    :param data: array of data (np.array) containing a single peak
    :return: amplitude of peak
    """


def is_tremor(frequency, amplitude, data):
    """
    Determine if data signal constitutes a tremor
    :param frequency: frequency (float) of tremor (Hz)
    :param amplitude: amplitude (float) of tremor
    :param data: array of data (np.array) containing single peak
    :return:
    """


def calc_PSF(data):
    """

    :param data:
    :return:
    """

if __name__ == "__main__":
    import numpy

    N = 400  # signal length of number
    x = numpy.arange(0, N, 1)  # generate the time ticks
    Sines = [numpy.sin(x * n) * (1 - n) for n in [.9, .75, .5, .25, .12, .03, 0.025]]  # different frequency components
    y = numpy.sum(Sines, axis=0)  # add them by column, low frequencies have higher amplitudes

    import matplotlib.pyplot as plt

    Low_cutoff, High_cutoff, F_sample = 5, 30, 500
    Spectrum, Filtered_spectrum, Filtered_signal, Low_point, High_point = bandpass_ifft(y, Low_cutoff, High_cutoff, F_sample)

    # plot raw data
    fig0 = plt.figure()
    plt.plot(x, y)

    # plot high filtered data
    fig1 = plt.figure()
    plt.plot(x, Filtered_signal)
    plt.show()

    pass
