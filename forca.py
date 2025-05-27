import random

def menssagem_inicial():
print("*********************************")
print("*** Bem-vindo ao jogo da Forca! ***")
print("*********************************")


def criar_palavra_secreta():

    
    

def define_letras_acertadas (palavras):
    palavras_acertadas = ["_"] * len(palavra_secreta)
    
    arquivo = open("neguin_enforca-main/palavras.txt","r")
    palavras =  []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    
    arquivo.close()
    
    
    
    aleatoria = random.randrange(0, len(palavras))
    palavra_secreta = palavras[aleatoria].upper()


def escreva_letra():
    chute = input("Qual é a letra? ")
    chute = chute.strip().upper()
    return chute
    
def jogar():
    

    

    
    enforcou = False
    acertou = False
    erros = 0 
    
    while not enforcou and not acertou:
        
        chute = escreva_letra()
        
        print(" ".join(letras_acertadas))  # Mostra as letras acertadas até agora
        
        
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
        print("Você perdeu BISCATE ! A palavra era:", palavra_secreta)
        
    print("Fim do jogo")

if __name__ == "__main__":
    jogar()