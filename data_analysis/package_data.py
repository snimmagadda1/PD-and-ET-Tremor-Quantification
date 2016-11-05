def extrapolate_accel_data(filename):
    """Extrapolate data from a txt file
    data will have format:
    x1,y1,z1;
    x2,y2,z2;
    ..
    xn,yn,zn;

    :param filename: file to read from
    :return: datax, datay, dataz vectors (np.array)
    """
    import numpy as np
    x = []
    y = []
    z = []
    chunk_size = 200
    conv_factor = 0.0039
    with open(filename, 'r') as f:
        filechunk = f.read(chunk_size)
        while len(filechunk) > 0:
            datapoints = re.findall('[\+|-].{13};', filechunk)
            for data in datapoints:
                components = data[:-1].split(',')
                x.append(float(components[0])*conv_factor)
                y.append(float(components[1])*conv_factor)
                z.append(float(components[2])*conv_factor)
            filechunk = f.read(chunk_size)
         
    return np.array(x), np.array(y), np.array(z)


if __name__ == "__main__":

    pass

