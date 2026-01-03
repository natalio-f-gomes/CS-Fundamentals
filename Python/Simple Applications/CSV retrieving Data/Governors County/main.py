import csv

def Governors_county(file):
    current_votes = file[2]
    total_votes = file[3]

    print("Current votes: " + current_votes)
    print("Total Votes: " + total_votes)

with open("governors_county.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    county = input("County: ")
    in_file = False
    for row in csv_reader:
        if (county == row[1]):
            Governors_county(row)
            in_file = True
    if not in_file:
        print("Not in file")

