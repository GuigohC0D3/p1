def jogar_forca():
    palavra_secreta = input("Digite a palavra secreta: ").lower()
    letras_descobertas = ['_'] * len(palavra_secreta)
    tentativas = 6
    letras_erradas = []

    while True:
        print("\nPalavra: " + " ".join(letras_descobertas))
        print("Tentativas restantes: " + str(tentativas))
        print("Letras erradas: " + " ".join(letras_erradas))

        if "_" not in letras_descobertas:
            print("Parabéns! Você venceu!")
            break

        if tentativas == 0:
            print("Game over! A palavra era: " + palavra_secreta)
            break

        letra = input("Digite uma letra: ").lower()

        if letra in letras_erradas or letra in letras_descobertas:
            print("Você já tentou essa letra. Tente novamente.")
            continue

        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    letras_descobertas[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas -= 1

jogar_forca()
