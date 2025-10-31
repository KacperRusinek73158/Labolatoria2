x =int(input("podaj x"))
y =int(input("podaj y"))
z =int(input("podaj z"))
kolejnosc =[]
if x<=y and x<=z:
    kolejnosc.append(x)
    if y<z:
        kolejnosc.append(y)
        kolejnosc.append(z)
    else:
        kolejnosc.append(z)
        kolejnosc.append(y)
elif y<=x and y<=z:
    kolejnosc.append(y)
    if x<z:
        kolejnosc.append(x)
        kolejnosc.append(z)
    else:
        kolejnosc.append(z)
        kolejnosc.append(x)
elif z<=x and z<=y:
    kolejnosc.append(z)
    if x<y:
        kolejnosc.append(x)
        kolejnosc.append(y)
    else:
        kolejnosc.append(y)
        kolejnosc.append(x)
else:
   print("sa rowne")
print(kolejnosc)
