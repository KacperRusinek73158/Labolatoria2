plik =open('notowania_gieldowe.txt','r')
print(plik.read())
plik.close()
#zadanie 5
plik =open('notowania_gieldowe.txt','a')

plik.write('\nALR, 113.')
plik.close()
plik =open('notowania_gieldowe.txt','r')
print(plik.read())
plik.close()
