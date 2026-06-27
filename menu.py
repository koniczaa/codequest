import json
import datetime
from dane import baza, exp_values, levels, format


def menu():
    czas = datetime.datetime.now()

    streak = 0
    global baza
    while True:
        baza["last save"] = str(datetime.datetime.today())
        date = datetime.datetime.strptime(baza["last save"], format)
        try:
            with open("data.json", "r") as f:
                baza = json.load(f)
                date = datetime.datetime.strptime(baza["last save"], format)

        except (FileNotFoundError, json.JSONDecodeError):
            pass
        if datetime.datetime.now().hour >= 6 and datetime.datetime.now().day > date.day:
            if (
                not baza["Read Kana"]
                and not baza["Solve Python Problem"]
                and not baza["Learn 10 Words"]
                and not baza["Read Japanese Pages"]
                and not baza["Japanese Listening"]
            ):
                baza["streak"] = 0
            else:
                baza["streak"] += 1
            for i in baza:
                if i not in ("xp", "last save", "streak"):
                    baza[i] = False

        for lvl in sorted(levels.keys(), reverse=True):
            if baza["xp"] >= levels[lvl]:
                print(f"Level {lvl}")
                break

        for i in baza:
            if i in ("last save", "streak", "xp"):
                continue
            if baza[i] == True:
                print(f"[✔] {i}")
            elif baza[i] == False:
                print(f"[ ] {i}")
        print(f"xp: {baza["xp"]}")
        print(f"lvl: {lvl}")
        print(f"streak: {baza["streak"]}")
        try:
            czyg = int(input("Which did you did?"))
            if czyg == 1 and not baza["Read Kana"]:
                baza["Read Kana"] = True
                baza["xp"] += exp_values["Read Kana"]
            elif czyg == 2 and not baza["Solve Python Problem"]:
                baza["Solve Python Problem"] = True
                baza["xp"] += exp_values["Solve Python Problem"]
            elif czyg == 3 and not baza["Learn 10 Words"]:
                baza["Learn 10 Words"] = True
                baza["xp"] += exp_values["Learn 10 Words"]
            elif czyg == 4 and not baza["Read Japanese Pages"]:
                baza["Read Japanese Pages"] = True
                baza["xp"] += exp_values["Read Japanese Pages"]
            elif czyg == 5 and not baza["Japanese Listening"]:
                baza["Japanese Listening"] = True
                baza["xp"] += exp_values["Japanese Listening"]
            elif czyg == 6:
                break

        except ValueError:
            print("Enter a number")
            pass

        zapis = json.dumps(baza, indent=5)
        with open("data.json", "w") as f:
            f.write(zapis)
