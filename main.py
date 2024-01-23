def jogar():
    print('*' * 20)
    print('Bem vindo ao Jogo da Forca')
    print('*' * 20)
    vidas = 5
    palavra_secreta = 'banana'
    letra_chutadas = []
    ganhou = False
    while True:
        for letra in palavra_secreta:
            if letra.lower() in letra_chutadas:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print(' ')
        tentativa = input('Digite a letra desejada: ')
        letra_chutadas.append(tentativa.lower())
        if tentativa.lower() not in palavra_secreta.lower():
            vidas -= 1
            print(f' voce tem {vidas} vidas')

        ganhou = True
        for letra in palavra_secreta:
            if letra.lower() not in letra_chutadas:
                ganhou = False
            
        
        if vidas == 0 or ganhou:
            break
        
        for letra in palavra_secreta:
            if letra == letra_chutadas:
                ganhou = True
                break
    if ganhou:
        print(f'Parabens voce acertou, a palavra era {palavra_secreta}')

    else:
        print(f'Voce perdeu e a palavra era {palavra_secreta}')


  

if (__name__=='__main__'):
    jogar()
    