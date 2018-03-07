import random
import csv

sampleSize = 500

x = []
y = []

for i in range(sampleSize):
    newVal = random.normalvariate(100,10)
    x.append(newVal)
    y.append(newVal / 2.0 + random.normalvariate(50,5))

with open("scatter1.csv", 'w+') as scatter:
    writer = csv.writer(scatter)
    writer.writerow(["x", "y"])
    for i in range(sampleSize):
        writer.writerow([x[i], y[i]])
