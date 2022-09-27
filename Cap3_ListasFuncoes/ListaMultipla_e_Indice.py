equipamento = []
valor = []
serial = []
departamento = []
resposta = "S"

while resposta =="S":
    equipamento.append(input("Equipamento: "))
    valor.append(input("Valor: "))
    serial.append(input("Serial: "))
    departamento.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar").upper()

for indice in range(0, len(equipamento)):
    print("Equipamento: ",(indice+1))
    print("Nome...........", equipamento[indice])
    print("valor..........", valor[indice])
    print("serial.........", serial[indice])
    print("departamento...",departamento[indice])

print()
print("FIM")