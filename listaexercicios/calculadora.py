import random

caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

quantidade = int(input("Quantos carcteres a senha deve ter?"))

senha = ""

for i in range(quantidade):
  senha += random.choice(caracteres)

  print(f"\nSenha gerada {senha}")
