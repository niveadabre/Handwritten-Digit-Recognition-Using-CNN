import numpy as np

cm = [[ 963,    0,    0,    1,    0,    2,   11,    1,    2,    0], 
        [   0, 1119,    3,    2,    1,    0,    4,    1,    4,    1],
        [  12,    3,  972,    9,    6,    0,    6,    9,   13,    2],
        [   0,    0,    8,  975,    0,    2,    2,   10,   10,    3],
        [   0,    2,    3,    0,  953,    0,   11,    2,    3,    8],
        [   8,    1,    0,   21,    2,  818,   17,    2,   15,    8],
        [   9,    3,    1,    1,    4,    2,  938,    0,    0,    0],
        [   2,    7,   19,    2,    2,    0,    0,  975,    2,   19],
        [   8,    5,    4,    8,    6,    4,   14,   11,  906,    8],
        [  11,    7,    1,   12,   16,    1,    1,    6,    5,  949]]

TP = np.diag(cm)
FP = np.sum(cm, axis=0) - TP
FN = np.sum(cm, axis=1) - TP

num_classes = 10
TN = []
for i in range(num_classes):
    temp = np.delete(cm, i, 0)    # delete ith row
    temp = np.delete(temp, i, 1)  # delete ith column
    TN.append(sum(sum(temp)))

l = 10000
for i in range(num_classes):
    print(TP[i] + FP[i] + FN[i] + TN[i] == l)

print ("TP")
print (TP)
print ("FP")
print (FP)

precision = TP/(TP+FP)
print (precision)

recall = TP/(TP+FN)
print (recall)