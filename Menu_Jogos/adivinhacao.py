# CODIGO BASE DE UM JOGO DE ADIVINHAÇÃO
#a ideia desse jogo e ter uma interação multiplayer ou 1 player que tem que advinhar qual um numero aleatório dentro deu um range determinado pelo nível de dificuldade do jogo
#as funções execuntam nessa sequencia manager_jogo() -> nivel_jogo() -> jogo_adivinhacao() - >pergunta_reiniciar_jogo() sendo manager_jogo() a responsável por acionar e adiministrar os recebiveis de info de cada uma das funções


#importa função para criar número aleatório
import random


#FUNÇÃO EXECUTADA NO FINAL DO JOGO PARA VALIDAR SE QUER REINICIAR O JOGO E VALIDAR SE A RESPOSTA ESTÁ CORRETA
def pergunta_reiniciar_jogo():
    while True:
        pergunta = input('Deseja reiniciar o jogo? Digite Y ou N: ')
        if pergunta.upper() in ['Y','N']:
            return pergunta
            break
        else:
            print('Digite Y ou N')


# FUNÇÃO QUE DETERMINA O NIVEL DE DIFICULDADE DO JOGO RANGE DE NUMERO PARA ADVINHAR E A QUANTIDADE DE TENTATIVAS
def nivel_jogo():
    while True:
        try:
          #recebe do usuário qual o nível de dificuldade que terá o jogo
            info_nivel = int(input('Digite o Nível do jogo (1 - Básico, 2 - Médio, 3 - Difícil) : '))
            if info_nivel == 1:
                tentativas = 3
                valor_maximo = 10
                break
            elif info_nivel == 2:
                tentativas = 5
                valor_maximo = 50
                break
            elif info_nivel == 3:
                tentativas = 10
                valor_maximo = 100
                break
            else:
                print('Digite entre 1 , 2 e 3')
        except ValueError:
            print('Digite somente um número inteiro')
    return tentativas,valor_maximo


# FUNÇÃO QUE EXECUTA O JOGO E DETERMINA A QUANTIDADE DE PONTOS CONQUISTADOS
def jogo_advinhacao(valor,tentativas,valor_maximo):

    #PONTOS BASE
    pontos = 1000
    pontos_perda = 0

    while True:
      # RECEBE OS VALORES VINDOS DA FUNÇÃO manager_jogo() que nela utiliza as informações que foi recebida de nível_jogo()
        valor, tentativas,valor_maximo = valor,tentativas,valor_maximo
        valor_range = 0
        print(f'Você terá {tentativas} tentativas para advinhar um número de 1 a {valor_maximo} \n Boa Sorte!')
        rodada = 1
        try:
          #loop que roda enquanto tiver tentativas disponíveis para o jogador
            while tentativas > 0:
                print(f'Estamos na {rodada}º rodada\n')
                palpite = int(input("Digite seu palpite: "))
                if palpite > valor_maximo  or palpite < 1:
                    print(f'Digite um valor menor ou igual a {valor_maximo}')
                    continue
              #valida se o jogador acertou determina os pontos finais dele e envia para manager_jogo()
                elif palpite == valor:
                    print(f'Parabéns, você acertou!! depois de {rodada} rodadas \n')
                    pontos -=pontos_perda
                    return pontos
                    break
                #função que da a instrução para o jogador quão distante ele está do número e faz a pontuação de quantos pontos ele perdeu
                elif palpite != valor:
                    valor_range = ((palpite /valor))*100
                    print(f"Seu palpite foi {valor_range:.2f}% do número secreto!, restam {tentativas} tentativas \n")
                  # a perda de pontos e baseada em quão distante foi o palpite do jogador
                    pontos_perda += abs(palpite-valor)

                tentativas -= 1
                rodada+=1

    # caso finalizar as tentativas sem acerto finaliza o loop da função informando qual era o número determina os pontos e envia para manager_jogo()
            if tentativas <= 0:
                print(f'Suas chances acabaram. O número era: {valor}\n')
                pontos -=pontos_perda
                return pontos

        except ValueError:
            print('Digite somente um número inteiro')


# FUNÇÃO BASE PARA COORDENAR TODO O JOGO
def manager_jogo():
#ABERTURA E INICIALIZAÇÃO DO JOGO
  print("Bem-vindo ao jogo de advinhação\n")
#Aciona a função nivel do jogo para definir quantidade de tentativas e valor maximo a ser adicionado
  tentativas,valor_maximo = nivel_jogo()
# gera o valor a ser adivinhado
  valor = random.randint(1, valor_maximo)

# loop para movimentar o jogo e também validar a quantidade de participantes
  while True:
    try:
  # difine quantidade de participantes do jogo
      quant_jogadores = int(input('Quantos jogadores participação? 1 ou 2: \n'))
#valida si tiver somente 1 jogador para operar o jogo somente 1 uvez
      if quant_jogadores == 1:

        jogador1_pontos = jogo_advinhacao(valor, tentativas,valor_maximo)
        print(f'você conquistou {jogador1_pontos} pontos')
        break
      #valida caso tenha 2 jogadores para dar a inicialização de do jogo para cada jogador e guarda os pontos somados
      elif quant_jogadores ==2:
        print('**** Inicia Jogo do jogador 1 **** \n')
        jogador1_pontos = jogo_advinhacao(valor, tentativas,valor_maximo)
        print(f'Jogador 1 você conquistou {jogador1_pontos} pontos\n')
        print('**** Inicia Jogo do jogodador 2 **** \n')
        valor2 = random.randint(1, valor_maximo)
        jogador2_pontos = jogo_advinhacao(valor2, tentativas,valor_maximo)
        print(f'Jogador 2 você conquistou {jogador2_pontos} pontos\n')

#valida qual jogador teve mais pontos e determina o vencedor
      if jogador1_pontos > jogador2_pontos:
        print('JOGADOR 1 FOI O VENCEDOR!! \n')
      elif jogador1_pontos == jogador2_pontos:
        print('TIVEMOS UM EMPATE!! \n')
      elif jogador2_pontos > jogador1_pontos:
        print('JOGADOR 2 FOI O VENCEDOR!\n')

#aciona função para reiniciar o jogo caso seja apontado Y
      reiniciar = pergunta_reiniciar_jogo()
      if reiniciar.upper() == 'N':
        break
      elif reiniciar.upper() =='Y':
        continue

    except ValueError:
      print('Digite somente um número inteiro entre 1 e 2')


#INICIALIZADOR DO JOGO
if __name__ == "__main__":
    manager_jogo()
