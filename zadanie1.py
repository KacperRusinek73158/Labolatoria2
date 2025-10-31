#zadanie 1
punkty= int(input("podaj ilość zdobytycych punktów"))
if punkty >= 80:
    print("Zaliczenie w terminie 0")
elif punkty < 80 and punkty >= 50:
    print("może poprawić")
else:
    print("musi poprawić ")
