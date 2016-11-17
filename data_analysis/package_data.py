def get_data(filename):
    """Extrapolate data from a txt file
        data will have format:
        x1,y1,z1;
        x2,y2,z2;
        ..
        xn,yn,zn;

        :param filename: file to read from
        :return: x, y, z vectors (np.array)
        """
    import re
    import numpy as np

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

    return np.array(x), np.array(y), np.array(z)

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
    pass

        

