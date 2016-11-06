def get_datachunk(f):
    """Extrapolate data from a txt file
    data will have format:
    x1,y1,z1;
    x2,y2,z2;
    ..
    xn,yn,zn;

    :param f: opened file to read from
    :return: datax, datay, dataz vectors (np.array)
    """
    import numpy as np
    import re
    x = []
    y = []
    z = []
    chunk_size = 480 # @ 120 Sa/s, returns about 4 seconds of data
    conv_factor = 0.0039 # ADC scale factor
    filechunk = f.read(chunk_size)
    if len(filechunk) > 0:
        datapoints = re.findall('[\+|-].{13};', filechunk)
        for data in datapoints:
            components = data[:-1].split(',')
            x.append(float(components[0])*conv_factor)
            y.append(float(components[1])*conv_factor)
            z.append(float(components[2])*conv_factor)       
        
        return {'x':x, 'y':y, 'z':z}
    else:
        return -1

def extrapolate_accel_data_testing(filename):
    """Extrapolate data from a txt file
    data will have format:
    x1,y1,z1;
    x2,y2,z2;
    ..
    xn,yn,zn;

    :param filename: file to read from
    :return: datax, datay, dataz vectors (np.array)
    """
    x = []
    y = []
    z = []
    import numpy as np
    with open(filename, 'r') as f:
        alllines = f.readlines()
        for line in alllines:
            components = line.split(',')
            sep = ';'
            cleaned_z = components[2].split(sep,1)[0]
            components[2] = cleaned_z
            x.append(float(components[0]))
            y.append(float(components[1]))
            z.append(float(components[2]))
    return np.array(x), np.array(y), np.array(z)

if __name__ == "__main__":
    import numpy as np
    import scipy
    import matplotlib.pyplot as plt
    from process_data import *
    # x = []
    # y = []
    # z = []
    # with open('data_rate_test.txt', 'r') as f:
    #     datachunk = get_datachunk(f)
    #     while (datachunk != -1):
    #         x.extend(datachunk['x'])
    #         y.extend(datachunk['y'])
    #         z.extend(datachunk['z'])
    #         datachunk = get_datachunk(f)

    x,y,z = extrapolate_accel_data_testing('sinusoid_8hz_fs_115.txt')
    filtcutoff = 14
    fs = 115
    filtx = butter_lowpass_IIR_filter(x, filtcutoff, 115)
    filty = butter_lowpass_IIR_filter(y, filtcutoff, 115)
    filtz = butter_lowpass_IIR_filter(z, filtcutoff, 115)

    enmofilt = remove_gravity_ENMO(filtx,filty,filtz)
    displacement = 1000*9.8*scipy.integrate.cumtrapz(enmofilt, x=[i/fs for i in range(len(enmofilt))],initial=0)

    # int_window = 5
    #
    # enmofilt = [e*9.8 for e in enmofilt] # conver to m/s^2
    #
    # velocity = [0 for i in range(0,len(enmofilt)-int_window)]
    # for i in range(int_window, len(enmofilt)):
    #     velocity[i-int_window] = np.trapz(enmofilt[i-int_window:i], x=None, dx=1/fs)
    #
    # displacement = [0 for i in range(0, len(velocity) - int_window)]
    # for i in range(int_window, len(velocity)):
    #     displacement[i - int_window] = np.trapz(velocity[i - int_window:i], x=None, dx=1 / fs)
    #
    # displacement = [d*1000 for d in displacement] # convert to mm

    plt.plot(displacement)
    plt.show()
        

