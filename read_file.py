import csv
import numpy as np
from numpy.core.fromnumeric import sort
from numpy.core.records import array
from scipy.sparse import data

from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

with open("credit_card_clients.csv", "r", encoding="utf8", newline="\r\n") as file:
    read_file = csv.reader(file)
    datas = np.array(list(read_file))

limit_to_age = datas[2:100, [1, 5]]

print(limit_to_age)
plt.title("LIMIT TO AGE")
plt.scatter(limit_to_age[:, 1], limit_to_age[:, 0])

plt.xlabel("AGE")
plt.ylabel("LIMIT")

plt.grid()

plt.show()
