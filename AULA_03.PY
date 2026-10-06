# for epoca in range(1, 11):
#     print(f"Treinando época {epoca}")
#----------------------------------------------------------
# temperaturas = [22.5, 24.8, 27.1, 23.9, 26.5]

# for temperatura in temperaturas:
#     print(f"Temperatura registrada: {temperatura}°C")
#----------------------------------------------------------
# temperaturas = [23.5, 25.2, 31.8, 24.1, 38.3]

# for temperatura in temperaturas:

#     if temperatura < 29:
#         print(f"{temperatura} → Temperatura normal")
#     else:
#         print(f"{temperatura} → ALERTA: temperatura elevada!")
#----------------------------------------------------------
# confiancas = [0.95, 0.65, 0.34, 0.82, 0.71]

# for confianca in confiancas:

#     if confianca >= 0.8:
#         print(f"{confianca} → Alta confiança")
#     elif confianca >= 0.5:
#         print(f"{confianca} → Confiança média")
#     else:
#         print(f"{confianca} → previsão com baixa confiança")
#----------------------------------------------------------
""" previsoes = [
    "gato",
    "cachorro",
    "gato",
    "pássaro",
    "gato",
    "cachorro"
]

quantidade = 0

for letra in previsoes:

    if letra == "gato":
        quantidade += 1

print(f"A palavra 'gato' apareceu {quantidade} vezes.") """
#----------------------------------------------------------
""" dados = [10, 15, 20, 25, 30]

soma= 0

for conta in dados:
    soma += conta

media = soma / len(dados)

print(f'A média é: {media}') """
#----------------------------------------------------------
""" dados = input("Digite uma frase: ")

quantidade = 0

for letra in dados:

    if letra == "a":
        quantidade += 1

print(f"A letra 'a' apareceu {quantidade} vezes.") """
#----------------------------------------------------------
""" dados = [12, 15, None, 18, None, 21]

for dado in dados:

    if dado is None:
        continue

    print(dado) """
#-------------------------DESAFIOS-------------------------#
""" previsoes = [
    0.92,
    0.84,
    0.35,
    0.76,
    0.28,
    0.95
]

for previsao in previsoes:

    if previsao < 0.30:
        print("Erro no sensor!")
        break

    print(f"As previsoes: {previsao}") """
#-----------------------------------------------------------
""" imagem = [
    [0, 255, 0],
    [255, 255, 0],
    [0, 0, 255]
]

for linha in imagem:

    for pixel in linha:
        print(pixel, end=" ")

    print() """
#-----------------------------------------------------------
""" previsoes = [
    "gato",
    "cachorro",
    "gato",
    "passaro",
    "gato",
    "cachorro"
]

gatos = 0
cachorros = 0
passaros = 0

for animal in previsoes:

    if animal == "gato":
        gatos += 1
    elif animal == "cachorro":
        cachorros += 1
    elif animal == 'passaro':
        passaros += 1

print(f"Gatos: {gatos}\nCachorros: {cachorros}\nPássaros: {passaros}") """
#-----------------------------------------------------------
""" objetos = [
    "pessoa",
    "carro",
    "pessoa",
    "bicicleta",
    "carro",
    "pessoa"
]

pessoas = 0

for detector in objetos:
    print(f'Objeto detectado: {detector}')
    if detector == 'pessoa':
        pessoas += 1

print(f'Total de pessoas detectadas: {pessoas}') """
#-----------------------------------------------------------