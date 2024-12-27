from random import choice

with open("palavra.txt") as arquivo:
    linhas = arquivo.read()
    lista_de_palavras = linhas.split("\n")

palavra = choice(lista_de_palavras).upper()

forca = """

"""""

vazio = """


"""

cabeca = """
    O
    
"""

tronco = """
    O
    | 
"""

braco_esquerdo = """
    O
   /|
"""

braco_direito = """
    O
   /|\\
"""

perna_esquerda = """
    O
   /|\\
   /  
"""

perna_direita = """
    O
   /|\\
   / \\
"""

boneco = [vazio, cabeca, tronco, braco_esquerdo, braco_direito, perna_esquerda, perna_direita]

print()

acertos = 0
erros = 0
letras_acertadas = ""
letras_erradas = ""

while acertos != len(palavra) or erros !=7:
    mensagem = ""
    for letra in palavra:
        if letra in letras_acertadas:
            mensagem += f'{letra}'
        else:
            mensagem += "_ "
    print(forca + boneco[erros])
    print(mensagem)

    letra = input("Digite uma letra: ").upper()

    if letra in letras_acertadas+letras_erradas:
        print("Essa letra ja foi burrão")
        continue

    if letra in palavra:
        print("Você acertou a letra")
        letras_acertadas += letra
        acertos += palavra.count(letra)
    else:
        print("Você errou a letra")
        letras_erradas += letra
        erros += 1
