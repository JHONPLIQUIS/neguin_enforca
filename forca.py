import random

def mensagem_inicial():
    print("*********************************")
    print("*** Bem-vindo ao jogo da Forca! ***")
    print("*********************************")

def criar_palavra_secreta():
    with open("neguin_enforca-main/palavras.txt", "r") as arquivo:
        palavras = [linha.strip().upper() for linha in arquivo]
    return random.choice(palavras)

def define_letras_acertadas(palavra_secreta):
    return ["_"] * len(palavra_secreta)

def escreva_letra():
    chute = input("Qual é a letra? ")
    return chute.strip().upper()

def jogar():
    mensagem_inicial()
    
    palavra_secreta = criar_palavra_secreta()
    letras_acertadas = define_letras_acertadas(palavra_secreta)
    
    enforcou = False
    acertou = False
    erros = 0 

    while not enforcou and not acertou:
        print(" ".join(letras_acertadas))  # Mostra as letras acertadas até agora
        chute = escreva_letra()
        
        if chute in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    letras_acertadas[index] = letra
        else:
            erros += 1 
            print(f"Você errou! Tentativas restantes: {10 - erros}")
        
        enforcou = erros == 10
        acertou = "_" not in letras_acertadas  # Verifica se todas as letras foram acertadas

    if acertou:
        print("Parabéns, você ganhou!")
    else:
        print(f"Você perdeu! A palavra era: {palavra_secreta}")
        
    print("Fim do jogo")

if __name__ == "__main__":
    jogar()