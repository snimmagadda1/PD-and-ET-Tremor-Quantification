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

def get_data(filename):
    """Extrapolate data from a txt file
        data will have format:
        x1,y1,z1;
        x2,y2,z2;
        ..
        xn,yn,zn;

        :param filename: file to read from
        :return: datax, datay, dataz vectors (np.array)
        """
    import re
    x = []
    y = []
    z = []
    chunk_size = 480  # @ 120 Sa/s, returns about 4 seconds of data
    conv_factor = 0.0039  # ADC scale factor
    with open(filename, 'r') as f:
        filedata = f.readline()
        datapoints = re.findall('[\+|-].{13};', filedata)
        for data in datapoints:
            components = data[:-1].split(',')
            x.append(float(components[0]) * conv_factor)
            y.append(float(components[1]) * conv_factor)
            z.append(float(components[2]) * conv_factor)

    return x, y, z

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
    import matplotlib
    matplotlib.use("TkAgg")
    import matplotlib.pyplot as plt
    from process_data import *


    x,y,z = get_data('data_rate_test.txt')

    filtcutoff = 14
    fs = 100
    filtx = butter_lowpass_IIR_filter(x, filtcutoff, fs)
    filty = butter_lowpass_IIR_filter(y, filtcutoff, fs)
    filtz = butter_lowpass_IIR_filter(z, filtcutoff, fs)

    accel = remove_gravity_ENMO(filtx,filty,filtz)

    print(get_disp_amplitude(np.array(accel), 1, 100))

    # convert to m^2 / s
    enmo = np.array(accel) * 9.8
    # recenter about 0
    enmo = enmo - np.mean(enmo)

    enmo_lowpassed = butter_highpass_IIR_filter(enmo, 2, 100)

    vel = scipy.integrate.cumtrapz(enmo_lowpassed, dx = 1/fs, initial=0)


    # recenter about 0

    vel = vel - np.mean(vel)

    vel_lowpassed = butter_highpass_IIR_filter(vel, 2, 100)

    disp = scipy.integrate.cumtrapz(vel_lowpassed, dx = 1/fs, initial=0)

    # recenter about 0

    disp = disp - np.mean(disp)

    # convert to mm

    disp = disp * 1000

    envelope_high = np.abs(scipy.signal.hilbert(disp))
    envelope_low = -1*np.abs(scipy.signal.hilbert(-1*disp))

    plt.subplot(411)
    plt.plot(accel)
    plt.title('raw acceleration')
    plt.subplot(412)
    plt.plot(enmo)
    plt.title('filtered acceleration recentered')
    plt.subplot(413)
    plt.plot(vel)
    plt.title('velocity recentered')
    plt.subplot(414)
    plt.plot(disp)
    plt.plot(envelope_high)
    plt.plot(envelope_low)
    plt.title('Displacement (mm)')
    plt.show()

        

