import random
import copy

x = []
y = []

with open("sonar_data.csv", "r") as file:
    for line in file:
        line = line.split(",")
        x.append([])
        for i in range(len(line)-1):
            x[-1].append(float(line[i]))

        y.append(int(line[-1]))


neurons = []
for i in range(60):
    neurons.append(random.uniform(-1,1))

offset = random.uniform(-1,1)


score = 0
while score < 120:
    score = 0
    for datapoint in range(len(x)):
        aitotal = 0
        for i in range(len(x[datapoint])):
            aitotal += x[datapoint][i] * neurons[i]

        if aitotal >= offset:
            if y[datapoint] == 1:
                score += 1

        if aitotal < offset:
            if y[datapoint] == 0:
                score += 1

    newneurons = []
    for i in neurons:
        newneurons.append(i + random.uniform(-1,1))
    newoffset = offset + random.uniform(-1,1)

    newscore = 0
    for datapoint in range(len(x)):
        aitotal = 0
        for i in range(len(x[datapoint])):
            aitotal += x[datapoint][i] * newneurons[i]

        if aitotal >= newoffset:
            if y[datapoint] == 1:
                newscore += 1

        if aitotal < newoffset:
            if y[datapoint] == 0:
                newscore += 1

    if newscore > score:
        neurons = copy.deepcopy(newneurons)
        offset = newoffset
        print(score)