import os
import csv
import funcs as f


while True:
    session = {}
    print(f"1.Add session\n2.View stats\n3.Exit")
    try:
        choice = int(input("Enter choice: "))

    except ValueError:
        os.system("cls")
        print("please enter your choice")
        continue


    if choice == 1:
        session["date"] = input("Enter date: ")
        session["attempts"] = int(input("Enter attempts: "))
        session["made"] = int(input("Enter made shots: "))
        session["duration"] = int(input("Enter duration in seconds: "))
        session["notes"] = input("Enter notes: ")

        percent = f.percentage(session["made"], session["attempts"])
        print(f"{percent}%")

        file_exists = os.path.exists("stats.csv")

        with open('stats.csv', 'a', newline='') as file:
            fieldnames = ["date", "attempts", "made", "duration", "notes"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow(session)

    elif choice == 2:
        file_exists = os.path.exists("stats.csv")

        if file_exists:
            with open('stats.csv', 'r', newline='') as file:
                data = csv.DictReader(file)
                for row in data:
                    print(
                        f"Date: {row['date']} |"
                        f"Attempts: {row['attempts']} |"
                        f"Made: {row['made']} |"
                        f"Duration: {row['duration']} sec |"
                        f"Notes: {row['notes']}"
                    )

        else:
            print("no stats given")
            continue

    elif choice == 3:
        os.system("cls")
        print("get out")
        break

    else :
        print("Invalid choice, choose among 1, 2, or 3")
        
