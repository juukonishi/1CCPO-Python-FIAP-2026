cp = 0

while cp <= 3:
    print(f"produto {cp}")
    cp += 1
cps = 4

while cps >= 1:
    print(f"produto {cps}")
    cps -= 1

jogar = "SIM"

while jogar.lower() == "sim":
    print("repete ou inicio do jogo")
    jogar = input("deseja jogar novamente? ")

i = 0
while i < 10:
    i += 1

    if i == 3 or i == 5:
        continue

    if i == 7:
        break

    print (f"Produto {i}")
