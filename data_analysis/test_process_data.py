def test_remove_nan():
    from process_data import remove_nan
    import numpy as np

    data = [2, 4, np.NaN, 3]

    out = remove_nan(data)

    assert out[0] == 2

    assert out[1] == 4

    assert out[2] == 3
