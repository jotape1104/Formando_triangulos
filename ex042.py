r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2 and r1 == r2 == r3:
    print('\033[4;32mAs três retas formam um triângulo e ele é um triângulo equilátero!')
elif r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2 and r1 == r2 or r1 == r3 or r2 == r1 or r2 == r3 or r3 == r1 or r3 == r2:
    print('\033[4;32mAs três retas formam um triângulo e ele é um triângulo isósceles!')
elif r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2 and r1 != r2 != r3:
    print('\033[4;32mAs três retas formam um triângulo e ele é um triângulo escaleno!')
else:
    print('\033[4;31mAs três retas não formam um triângulo!')