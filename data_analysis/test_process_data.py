def test_remove_nan():

    pass


def test_integrate_time_series():

    pass


def test_bandpass_ifft():
    from process_data import bandpass_ifft
    from test_signal1 import test_signal
    signal = test_signal()
    Spectrum, Filtered_spectrum, Filtered_signal, Low_point, High_point = bandpass_ifft(signal,0.25,50,16)
    print(Filtered_signal)

def test_calc_amplitude():

    pass


def test_is_tremor():

    pass


def test_psd_welch():

    pass


def test_gs_to_accel():

    pass


def test_calculate_magnitude_acceleration():

    pass

def test_remove_gravity_ENMO():

    pass


def test_remove_gravity_HFEN():

    pass

if __name__ == "__main__":
    test_bandpass_ifft()



