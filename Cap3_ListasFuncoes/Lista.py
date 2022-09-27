inventario = []
resposta ="S"

while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(input("Raridade: "))
    inventario.append(int(input("Numero Serial: ")))
    resposta = input("Digite \"S\"para continuar: ").upper()

for element in inventario:
    print(element)
