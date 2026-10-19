""" idade = int(input("Digite um número: "))

if idade < 12:
    print("Criança")

elif idade >= 12 and idade < 17:
    print("Adolescente")

elif idade >= 18 and idade < 59:
    print("Adulto")

else:
    print("idoso") """

# -------------------- / -------------------- #

""" lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 == lado2 and lado1 == lado3:
    print('Equilatero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Isósceles')
else:
    print('Escaleno') """

# -------------------- / -------------------- #

""" compra = float(input('Digite o valor da sua compra: '))
desconto = 0
valor_desconto = 0
valor_final = 0

if compra > 500:
    desconto = 15
elif compra >= 300:
    desconto = 1
elif compra > 100:
    desconto = 5
else:
    desconto = 0

valor_final = compra - (desconto * (compra/100))

print(f'Valor da compra: {compra}')
print(f'Desconto: R$ {desconto}%')
print(f'valor desconto: R${compra - valor_final}')
print(F'Valor final: R${valor_final}') """

# -------------------- / -------------------- #

valor_compra = float(input("Valor da compra: R$ "))

if valor_compra <= 100:
    percentual_desconto = 0
elif valor_compra <= 300:
    percentual_desconto = 5
elif valor_compra <= 500:
    percentual_desconto = 10
else:
    percentual_desconto = 15

valor_desconto = valor_compra * percentual_desconto / 100
valor_final = valor_compra - valor_desconto

print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto: {percentual_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")

# -------------------- / -------------------- #

nota = float(input("Digite sua nota: "))
frequencia = float(input("Digite sua frequência (%): "))

if frequencia < 75:
    print("Reprovado por frequência")
else:
    if nota >= 7:
        print("Aprovado")
    elif nota >= 5:
        print("Recuperação")
    else:
        print("Reprovado")

# -------------------- / -------------------- #

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")

# -------------------- / -------------------- #

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# -------------------- / -------------------- #

nivel = int(input("Digite o nível do personagem: "))
possui_espada = input("Possui espada? (s/n): ").lower() == "s"
possui_cajado = input("Possui cajado? (s/n): ").lower() == "s"

if nivel >= 10 and (possui_espada or possui_cajado):
    print("Pode entrar na dungeon.")
else:
    print("Não pode entrar na dungeon.")

# -------------------- / -------------------- #

import random

print("0 - Pedra")
print("1 - Papel")
print("2 - Tesoura")

jogador = int(input("Escolha uma opção: "))
computador = random.randint(0, 2)

opcoes = ["Pedra", "Papel", "Tesoura"]

if jogador < 0 or jogador > 2:
    print("Opção inválida.")
else:
    print(f"Você escolheu: {opcoes[jogador]}")
    print(f"Computador escolheu: {opcoes[computador]}")

    if jogador == computador:
        print("Empate!")
    elif (jogador == 0 and computador == 2) or \
         (jogador == 1 and computador == 0) or \
         (jogador == 2 and computador == 1):
        print("Vitória!")
    else:
        print("Derrota!")

# -------------------- / -------------------- #

usuario_correto = "admin"
senha_correta = "1234"

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == usuario_correto:
    if senha == senha_correta:
        print("Login realizado com sucesso")
    else:
        print("Senha incorreta")
else:
    print("Usuário incorreto")