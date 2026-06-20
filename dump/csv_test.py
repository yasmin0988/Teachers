import csv

made = int(input("Enter made shots: "))
attempt = int(input("Enter attempts: "))

with open('bball.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([made, attempt])

with open('bball.csv', "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)