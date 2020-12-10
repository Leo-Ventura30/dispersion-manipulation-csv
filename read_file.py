import csv

with open("credit_card_clients.csv", "r", encoding="utf8", newline="\r\n") as file:
    read_file = csv.reader(file)
    datas = list(read_file)


for row in datas[:10]:
    print(row)