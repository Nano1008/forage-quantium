import csv


# keep pink morsels product and calculate every sales
def getData(file):
    data = []
    with open(file) as file1:
        reader = csv.DictReader(file1)
        for row in reader:
            if row["product"] == "pink morsel":
                d = {}
                d["sales"] = float(row["price"][1:]) * float(row["quantity"])
                d["date"] = row["date"]
                d["region"] = row["region"]
                data.append(d)
        return data

data1 = getData("data/daily_sales_data_0.csv")
data2 = getData("data/daily_sales_data_1.csv")
data3 = getData("data/daily_sales_data_2.csv")
dataSum = data1 + data2 + data3

# output a csv file
header = ["sales", "date", "region"]

with open("daily_sales_data_pink_morsels.csv", newline="", mode="w") as f:
    writer = csv.DictWriter(f, header)
    writer.writeheader()
    writer.writerows(dataSum)

