gol=int(input("podaj ilość goli"))
bonus=0
punkty =0
punkty+=(gol*10)
if gol >= 5:
    bonus+=5
if gol>10:
    bonus+=10
print("bonus=",bonus)
punkty+=bonus
print("punkty=",punkty)

