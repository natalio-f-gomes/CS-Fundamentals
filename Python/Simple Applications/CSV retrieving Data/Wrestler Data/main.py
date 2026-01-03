import csv

def Wrestler(wrestler_data):
  total = int(wrestler_data[1]) + int(wrestler_data[2]) + int(wrestler_data[3])
  wins = int(wrestler_data[1]) / total * 100
  losses = int(wrestler_data[2]) / total*100
  draws = int(wrestler_data[3]) / total*100
  print(f"Wrestler's name: {wrestler_data[0]}")
  print(f"Wins percentage: {round(wins)}%")
  print(f"Losses percentage: {round(losses)}%")
  print(f"Draws percentage: {round(draws)}%")
  
with open('Resources/WWE-Data-2016.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter= ',')
  check = input("What wrestler are you looking for? \nA: ")
  found = False
  for row in csv_reader:
    if check == row[0]:
      Wrestler(row)
      found = True
  if not found:
    print('Name not found')
