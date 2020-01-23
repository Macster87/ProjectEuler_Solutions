summe = 0

ersteZahl = 0
zweiteZahl = 1

while zweiteZahl < 4000000:
    fibo = ersteZahl + zweiteZahl
    if fibo%2 == 0:
        summe = summe + fibo
    ersteZahl = zweiteZahl
    zweiteZahl = fibo

print(summe)
#