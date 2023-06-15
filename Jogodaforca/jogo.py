palavra = input('Digite uma palavra: ')
lista = list(palavra)
contAcertoRestante = 0
contErroRestante = 5
i = 0
     
while contErroRestante != 0 and contAcertoRestante != len(lista)-1:
    
    letra = input('Digite uma letra: ')
    
    acertoRestanteInicial = contAcertoRestante
    
    for i in range(len(lista)):
        
        if  lista[i] == letra:
            contAcertoRestante = contAcertoRestante+1
            print(f"A letra {letra}, está na posição: {i}, você tem mais {len(lista)-1-contAcertoRestante} letras antes de arriscar a palavra.")
            
    if(contAcertoRestante == acertoRestanteInicial):
        
        contErroRestante = contErroRestante-1 
        print(f"A letra inserida não pertence a palavra, erros restantes: {contErroRestante}")
        if(contErroRestante == 0):
            print("Você Perdeu!")  
    
    if (contAcertoRestante == len(lista)-1):
        palavraFinal = input("Digite sua palavra: ")
        if (palavraFinal == palavra):
            print("Parabéns, você ganhou!")
            contErroRestante = 0
        else:
            print(f"Sinto muito, a palavra correta era: {palavra}")
            contErroRestante = 0
    i += 1
    
if(contErroRestante != 0):
    
    palavraFinal = input("Digite sua palavra: ")
    if (palavraFinal == palavra):
        print("Parabéns, você ganhou!")
    else:
        print(f"Sinto muito, a palavra correta era: {palavra}")