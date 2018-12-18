i = 1
ersteSumme = 0
zweiteSumme = 0

while i <= 100:
    zweiteSumme = zweiteSumme + i
    ersteSumme = ersteSumme + i**2
    i = i + 1

zweiteSumme = zweiteSumme**2

print(zweiteSumme - ersteSumme)

