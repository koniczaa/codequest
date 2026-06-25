import json


def menu():
    print(
        "Today's missions\n\n1.[ ] Read Kana\n2.[ ] Solve Python Problem\n3.[ ] Learn 10 Words\n4.Exit"
    )
    baza = {"Read Kana": False, "Solve Python Problem": False, "Learn 10 Words": False}
    while True:
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


menu()
