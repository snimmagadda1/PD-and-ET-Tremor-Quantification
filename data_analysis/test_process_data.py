import numpy as np
from process_data import *

def test_remove_nan():
    test_data = np.array([1,2,3,float('Nan'),9,15.0,'i',float('Nan')])
    nan_removed = remove_nan(test_data)
    should_be = np.array([1,2,3,9,15.0,'i'])
    assert np.array_equal(nan_removed,should_be)


def test_meters_to_mm():
    test_data = [2,3,4.5,1000,0]
    should_be = np.array([2000,3000,4500,1000000,0])
    output = meters_to_mm(test_data)
    assert np.array_equal(should_be,output)

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


def test_calculate_magnitude_acceleration():

    pass

def test_remove_gravity_ENMO():

    pass


def test_remove_gravity_HFEN():

    pass

if __name__ == "__main__":
    test_remove_nan()
    test_meters_to_mm()



