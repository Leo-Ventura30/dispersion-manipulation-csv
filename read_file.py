import csv
import numpy as np

from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

with open("credit_card_clients.csv", "r", encoding="utf8", newline="\r\n") as file:
    read_file = csv.reader(file)
    datas = np.array(list(read_file))

kmeans = KMeans(n_clusters=5,  # numero de clusters
                # algoritmo que define a posição dos clusters de maneira mais assertiva
                init='k-means++', n_init=100,
                max_iter=1)
limit_to_age = datas[2:100, [1, 5]]
pred_y = kmeans.fit_predict(limit_to_age)

print(limit_to_age)
plt.title("LIMIT TO AGE")
plt.scatter(limit_to_age[:, 1], limit_to_age[:, 0], c=pred_y)

plt.xlabel("AGE")
plt.ylabel("LIMIT")
plt.grid()
plt.show()
