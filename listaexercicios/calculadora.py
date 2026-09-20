nome = input("Nome: ")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    situacao = "Abaixo do peso"
elif imc < 25:
    situacao = "Peso normal"
elif imc < 30:
    situacao = "Sobrepeso"
else:
    situacao = "Obesidade"

print(f"\n{nome}, seu IMC é {imc:.2f}")
print(f"Classificação: {situacao}")
