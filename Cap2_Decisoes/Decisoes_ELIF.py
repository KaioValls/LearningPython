nome=input("Nome: ")
idade = int(input("Idade: "))
doencaContagiosa = input("Possui doença contagiosa?(sim || não) ").upper()

if idade>= 65:
    print("O paciente", nome,"possui atendimento prioritário.")
elif doencaContagiosa=="SIM":
    print("O paciente",nome,"deve ser levado a UTI.")
else :
    print("O paciente",nome ,"não possui atendimento prioritário")
