import json


def menu():

    baza = {"Read Kana": False, "Solve Python Problem": False, "Learn 10 Words": False}
    while True:
        try:
            with open("data.json", "r") as f:
                baza = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

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
        zapis = json.dumps(baza, indent=3)
        with open("data.json", "w") as f:
            f.write(zapis)


menu()
