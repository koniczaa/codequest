import json
import datetime


def menu():
    czas = datetime.datetime.now()

    baza = {
        "Read Kana": False,
        "Solve Python Problem": False,
        "Learn 10 Words": False,
        "Read Japanese Pages": False,
        "Japanese Listening": False,
        "xp": 0,
    }

    format = "%Y-%m-%d %H:%M:%S.%f"
    baza["last save"] = str(datetime.datetime.today())
    date = datetime.datetime.strptime(baza["last save"], format)

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
            if i == "last save":
                continue
            if baza[i] == True:
                print(f"[✔] {i}")
            elif baza[i] == False:
                print(f"[ ] {i}")
            else:
                print(f"you'r xp is {baza["xp"]}")

        try:
            czyg = int(input("Which did you did?"))
            if czyg == 1:
                baza["Read Kana"] = True
                baza["xp"] += 30
            elif czyg == 2:
                baza["Solve Python Problem"] = True
                baza["xp"] += 50
            elif czyg == 3:
                baza["Learn 10 Words"] = True
                baza["xp"] += 40
            elif czyg == 4:
                baza["Read Japanese Pages"] = True
                baza["xp"] += 100
            elif czyg == 5:
                baza["Japanese Listening"] = True
                baza["xp"] += 80
            elif czyg == 6:
                break
        except ValueError:
            print("Enter a number")
            pass

        zapis = json.dumps(baza, indent=5)
        with open("data.json", "w") as f:
            f.write(zapis)


menu()
