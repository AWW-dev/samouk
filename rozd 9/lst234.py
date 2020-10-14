import csv

# with open("st.csv", "w", newline='') as f:
#     write = csv.writer(f, delimiter=",")
#     write.writerow(["jeden",
#                     "dwa",
#                     "trzy"])
#     write.writerow(["cztery",
#                     "piec",
#                     "szesc"])

with open("st.csv", 'r') as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print (",".join(row))