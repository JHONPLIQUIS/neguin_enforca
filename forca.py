def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    
    palavra_secreta = "yamal"
    
    enforcou = False
    acertou = False
    
    while (not enforcou and not acertou):
        chute = input("qual é a letra?")
        
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print(chute)
                index = index + 1 
                
        print("jogando...")
        
        
        
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
