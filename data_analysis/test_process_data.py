def test_remove_nan():
    from process_data import remove_nan
    import numpy as np

    data = [2, 4, np.NaN, 3]

    out = remove_nan(data)

    assert out[0] == 2

    assert out[1] == 4

    assert out[2] == 3


def test_integrate_time_series():

    pass


def test_bandpass_ifft():

    pass


def test_calc_amplitude():

    pass


def test_is_tremor():

    pass


def test_psd_welch():

    pass


def test_gs_to_accel():

    pass


def test_remove_gravity_ENMO():

    pass


def test_remove_gravity_HFEN():

    pass





