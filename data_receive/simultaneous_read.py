def read_csv():
    import csv
    print("READING CSV")
    with open('output.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def write_csv():
    import csv, random

    RESULTS1 = random.sample(range(1, 10000), 1000)
    RESULTS2 = random.sample(range(1, 10000), 1000)
    RESULTS3 = random.sample(range(1, 10000), 1000)
    resultFile = open("output.csv", 'w')
    wr = csv.writer(resultFile)
    wr.writerow(RESULTS1)
    wr.writerow(RESULTS2)
    wr.writerow(RESULTS3)

if __name__ == "__main__":
    from multiprocessing import Process

    p1 = Process(target=write_csv())
    p1.start()
    p2 = Process(target=read_csv())
    p2.start()

