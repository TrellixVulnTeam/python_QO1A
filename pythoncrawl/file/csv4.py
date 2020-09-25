import csv

with open("./resources/sample3.csv", "r") as f:
    reader = csv.DictReader(f)

    next(reader)  # 헤더명 없애기

    for c in reader:
        print(c)
        for k, v in c.items():
            print(k, v)
        print("---------------")
