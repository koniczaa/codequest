import json
import datetime


def menu():
    czas = datetime.datetime.now()
    baza = {"Read Kana": False, "Solve Python Problem": False, "Learn 10 Words": False}
    format = "%Y-%m-%d %H:%M:%S.%f"
    while True:
        try:
            with open("data.json", "r") as f:
                baza = json.load(f)
                date = datetime.datetime.strptime(baza["last save"], format)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        if datetime.datetime.now().hour >= 6 and datetime.datetime.now().day > date.day:
            for i in baza:
                baza[i] = False
        for i in baza:
            if baza[i] == True:
                print(f"[✔] {i}")
            else:
                print(f"[ ] {i}")

        try:
            czyg = int(input("Which did you did?"))
            if czyg == 4:
                break
            if czyg == 1:
                baza["Read Kana"] = True
            elif czyg == 2:
                baza["Solve Python Problem"] = True
            elif czyg == 3:
                baza["Learn 10 Words"] = True
        except ValueError:
            print("Enter a number")
            pass

        baza["last save"] = str(datetime.datetime.today())

        zapis = json.dumps(baza, indent=3)
        with open("data.json", "w") as f:
            f.write(zapis)


menu()
