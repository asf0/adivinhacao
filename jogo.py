import funcoes

tentativas = int
cont_tent = 0

while True:
    diff = int(input("Dificuldade:\n[1] Fácil\n[2] Médio\n[3] Hard\n"))
    if 1 <= diff <= 3:
        tentativas = funcoes.diffop(diff)
        break
    else:
        print('Opção Invalida\nTente Novamente')

while True:
    palavra_tema = int(input("Temas:\n[1] Cidades\n[2] Cores\n[3] Nomes\n"))

    if 1 <= palavra_tema <= 3:
        palavra = funcoes.tema(palavra_tema)
        break
    else:
        print('Opção Invalida\nTente Novamente')

print(f"Sua palavra embaralhada é {funcoes.embaralha(palavra)}")
while True:
    chute = str(input("Tente descobrir a palavra: "))
    cont_tent += 1
    if palavra == chute:
        print("Parabens")
    elif palavra != chute:
        print(funcoes.msg_pos())
    if cont_tent >= tentativas or palavra == chute:
        break

print(f"Você tentou {cont_tent} vezes")

