def read_csv():
    import csv
    import datetime

    datetime.datetime.now().time()
    print(str(datetime.datetime.now().time()) + " READING CSV")

    with open('output.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def write_csv():
    import csv, random
    import datetime

    datetime.datetime.now().time()
    print(str(datetime.datetime.now().time()) + " WRITING CSV")

    RESULTS1 = random.sample(range(1, 10000), 1000)
    RESULTS2 = random.sample(range(1, 10000), 1000)
    RESULTS3 = random.sample(range(1, 10000), 1000)
    resultFile = open("output.csv", 'w')
    wr = csv.writer(resultFile)
    wr.writerow(RESULTS1)
    wr.writerow(RESULTS2)
    wr.writerow(RESULTS3)


from time import sleep
import subprocess
import threading


def runmodels(arg):

    subprocess.call(arg, shell=True)
    sGlobal.release() # release for next launch

if __name__ == "__main__":
    from multiprocessing import Process
    import time



    p1 = Process(target=write_csv())
    p1.start()
    #time.sleep(10)
    p2 = Process(target=read_csv())
    p2.start()


