import random
from time import sleep

print('           ---------\n           |  JO   |\n           |  KEN  |\n           |  PÔH! | \n           ---------')
print("\nEai, vamos jogar Pedra, Papel ou Tesoura?!")
sleep(0.7)#tempo de 7 milesimos de segundos
res = str(input("Aperte 's' para aceitar ou QUALQUER outra tecla para recusar\n")).lower()
if res != 's' and res != 'sim':#se não aceitarmos o desafio
    print('IIIIIH, PIPOCOU !!!')
else:#se aceitar, executa tudo abaixo.
    print('\nENTÃO VAMOS COMEÇAR!!! \n')
    sleep(2)#tempo de 2 segundos
    print('JO...')
    sleep(0.8)#tempo de 8 milesimos de segundos
    print('     KEN...')
    sleep(1)#tempo de 1 segundo
    
    opcao = ['Pedra', 'Papel', 'Tesoura']#opções
    print(f'Escolha uma opção: \n(1) Pedra \n(2) Papel \n(3) Tesoura ')
    jogador = input(f'(1)Pedra   (2)Papel   (3)Tesoura \n').capitalize()#aqui o jogador escolhe uma opção.
    if jogador == '1' or jogador == 'Pedra':#se aperta 1 ou escrever pedra, jogador recebe pedra.
        jogador = 'Pedra'
        #print(jogador)
    elif jogador == '2' or jogador == 'Papel':#se apertar 2 ou escrever papel, jogador recebe papel
        jogador = 'Papel'
        #print(jogador)
    elif jogador == '3' or jogador == 'Tesoura':#se apertar 3 ou escrever tesoura, jogador recebe tesoura
        jogador = 'Tesoura'
        #print(jogador)
            
    computador = random.choice(opcao)#aqui o computador escolhe uma das opções aleatoriamente
    print(' \n...PÔH !!! \n')

    if computador == jogador:#se PC e Jogador escolher igual da empate
        print('EMPATOU')
        #Condição de Vitoria do JOGADOR    
    elif computador == 'Pedra' and jogador == 'Papel':#se PC escolhe pedra e jogador escolhe papel, jogador vence!
        print('Jogador venceu!')
    elif computador == 'Papel' and jogador == 'Tesoura':#se PC escolhe papel e jogador escolhe tesoura, jogador vence!
        print('Jogador venceu!')  
    elif computador == 'Tesoura' and jogador == 'Pedra':#se PC escolhe tesoura e jogador escolhe pedra, jogador vence!
        print('Jogador venceu!')
        #Condição de vitoria do PC    
    elif jogador == 'Pedra' and computador == 'Papel':#se Jogador escolhe pedra e PC escolhe papel, PC vence!
        print('Computador venceu!')
    elif jogador == 'Papel' and computador == 'Tesoura':#se Jogador escolhe papel e PC escolhe tesoura, PC vence!
        print('Computador venceu!')  
    elif jogador == 'Tesoura' and computador == 'Pedra':#se Jogador escolhe tesoura e PC escolhe pedra, PC vence!
        print('Computador venceu!')

    else:
        print('ERRO !!! \nVocê não digitou uma opção valida.')#Caso digite algo de errado.

    print(f'Computador escolheu: {computador}')#Mostra a esolha do PC
    print(f'jogador escolheu: {jogador}')#Mostra a escolha do Jogador

#Implementar uma repetição caso o jogador digite uma opção invalida. || STATUS: A FAZER...
#Implementar CORES (\033[m). || STATUS: A FAZER...