# JOGO DA FORCA!

#pagina que gera palavra aleatória com a dica de definição
import busca_palavra_secreta
import random

#função para contar quantas letras ainda faltam na palavra
def contar_elementos(palavra_chute, elemento=' _ '):
    return palavra_chute.count(elemento)

#FUNÇÃO EXECUTADA NO FINAL DO JOGO PARA VALIDAR SE QUER REINICIAR O JOGO E VALIDAR SE A RESPOSTA ESTÁ CORRETA
def pergunta_reiniciar_jogo():
    while True:
        pergunta = input('Deseja reiniciar o jogo? Digite Y ou N: ')
        if pergunta.upper() in ['Y','N']:
            return pergunta
        else:
            print('Digite Y ou N')


#função para perguntar se deseja uma dica da palavra gerando retorno Y ou N para executar a função de gerar o significado
def pergunda_dica(palavra_chute):
        while True:
            pergunta = input(f'Deseja saber o significado da palavra {" ".join(palavra_chute)}? Digite Y ou N se sim - 15 pontos : ')
            if pergunta.upper() in ['Y', 'N']:
                return pergunta
                break
            else:
                print('Digite Y ou N')


#função para perguntar se deseja chutar qual a palavra secreta e envia Y ou N para gerar a função chutar palavra
def pergunda_chutar_palavra(palavra_chute):

    while True:
        pergunta = input('Deseja chutar qual é a palavra? Digite Y ou N: ')
        if pergunta.upper() in ['Y', 'N']:
            return pergunta
            break
        else:
            print('Digite Y ou N')

# função que recebendo Y ou N necessita chutar a palavra
def chutar_palavra(perg_chute,palavra_secreta,palavra_chute):
    pontos_de_chute = 0
    if perg_chute.upper() == 'Y':
        chute_palavra = input(f'Qual é a palavra?{"".join(palavra_chute)} : ')

        if chute_palavra.upper() == palavra_secreta.upper():
            print("PARABÉNS! VOCÊ ACERTOU A PALAVRA SECRETA")
            acertou = True
            pontos_de_chute+=20
            return acertou,pontos_de_chute
        else:
            print(f'Que pena você errou! a palavra era: {palavra_secreta}')
            enforcou = True
            pontos_de_chute -=50
            return enforcou,pontos_de_chute
    if perg_chute.upper() == 'N':
        return None,pontos_de_chute

# função que envia o significado da palavra quando recebe o Y
def gerar_significado(pergunta_dica,significado,palavra_chute):
    if pergunta_dica.upper() == 'Y':
        return print(f'Significado da palavra {" ".join(palavra_chute)}: {significado}\n')

#função para escolher uma palavra dentro de um arquivo salvo na pasta
def escolher_palavra():
    lista_palavras = []
    # Utilizando a abertura do arquivo com a codificação UTF-8
    with open('lista_palavras.txt','r',encoding='utf-8') as arquivo:
    #loop para valida cada linha do arquivo e adiciona na lista
        for linha in arquivo:
            linha = linha.strip()
            lista_palavras.append(linha)
    #escolhe aleatoriamente uma palavra
    palavra_escolhida = random.choice(lista_palavras)
    arquivo.close()
    return palavra_escolhida

#Função para Imprimir dicas sobre as palavra
def imprimir_dicas(palavra_secreta, sinonimos):
    print("*********************************")
    print("DICAS: ")
    print(f'A palavra secreta tem {len(palavra_secreta)} letras')
    print(f'Sinônimos da palavra são: {sinonimos}')
    print("*********************************")

#imprime a quantidade atual de pontos do usuário
def imprimir_pontuacao(pontos):
    print(f'Sua pontuação atual é: {pontos}')
    print("*********************************")



# função geal que efetua o jogo por inteiro
def jogar(palavra_secreta,significado,sinonimos,nivel_do_jogo):


#variaveis do jogo:

#lista para armazenar as letras corretas e comparar final com a palavra secreta
    palavra_chute = [' _ '] * len(palavra_secreta)
#lista para adicionar todas as letras incorretas que foram chutadas
    letras_chute_incorreta = []
#variaveis determinates para finalizar o jogo finaliza quando uma das 2 for verdadeira
    acertou = False
    enforcou = False

#variavel que determina a pontuação de cada jogador
    pontos = 1000

# Ajuste as penalidades e recompensas de acordo com a dificuldade do nível escolhido.
    if nivel_do_jogo == 1:
        pontos -= 10  # Ajuste conforme necessário
    elif nivel_do_jogo == 2:
        pontos -= 20  # Ajuste conforme necessário

#determina a quantidade de tentativas de erro disponiveis de acordo com o tamanho da palavra
    tentativas_erros = 7 if len(palavra_secreta)>8 else 3
# garante que poderá visualizar o significado da palavra somente uma vez
    uso_significado = 1


    print(f'Você poderá errar até {tentativas_erros} vezes seu palpite!\n')
    imprimir_dicas(palavra_secreta, sinonimos)

   # loop para rodar todo o jogo enquantdo a variavel acertou ou enforcou serem falsas
    while not enforcou and not acertou:
        # pergunta qual a palavra trazendo o adicional de quantidade de letras
        imprimir_pontuacao(pontos)
        chute = str(input(f'Qual letra você acha que tem nessa palavra: {" ".join(palavra_chute)} '))
        #condição para garantir que só terá 1 caracter no chute
        if len(chute)>1:
            print('Por gentileza digitar somente 1 caracter!')
            continue
# função para remover espaços em branco do inicio e fim da letra
        chute = chute.strip()
        #variavel para caso errar a letra nas funções abaixo deduzir a quantidade restante de tentativas
        acertou_letra = False
        #função para saltar o loop caso aponte uma letra que ja foi utilizada que era correta
        if chute in palavra_chute or chute in letras_chute_incorreta:
            print('Essa letra já foi escolhida! por favor tente novamente\n')
            acertou_letra = True
            continue

        # inicia aqui o loop de verificação das letras
        try:
            index = 0

            # loop para validar o chute de letra dado e já anota dentro da lista qual posição da letra que foi chutada
            for letra in palavra_secreta:
                if letra.upper() == chute.upper():  # upper para deixar ambos com letra maiúscula
                    palavra_chute[index] = chute
                    acertou_letra = True
                index += 1
            #informa quantas letras faltam preencher
            print(f' ainda faltam {contar_elementos(palavra_chute)} letras para descobrir')

            # adiciona as letras chutadas que eram incorretas dentro da listra para posteriormente validar se ja foram jogadas ou não
            if chute.upper() not in palavra_secreta.upper():
                letras_chute_incorreta.append(chute)

# valida se todas as letras foram encontrada
            if contar_elementos(palavra_chute) == 0:
                print(f'Parabéns você encontrou todas as letras da palavra secreta! a palavra era{"".join(palavra_chute)}')
                acertou = True
                break

            #valida que se tiver poucas letras faltantes ou somente 2 tentativas de erro a possibilidade de ver o significado da palavra e também chutar qual é a palavra
            if contar_elementos(palavra_chute) <= len(palavra_secreta)*0.2 or tentativas_erros <= 2:

                #valida se tem saldo para usar a dica e executa se quer utilizar
                if uso_significado == 1:
                    pergunta_dica = pergunda_dica(palavra_chute)

                #faz a execução do lançamento do significado da palavra canso a resposta for Y e tiver crédito deduz 15 pontos
                if pergunta_dica.upper() == 'Y' and uso_significado == 1:
                    gerar_significado(pergunta_dica,significado,palavra_chute)
                    uso_significado -= 1
                    pontos -= 15


                #valida se a pessoa que fazer o chute sobre a palavra
                perg_chute = pergunda_chutar_palavra(palavra_chute)
                #executa a validação se a palavra chutava está correta
                resultado_perg_chute,retorno_chute = chutar_palavra(perg_chute, palavra_secreta, palavra_chute)
                pontos+= retorno_chute
                if resultado_perg_chute is not True:
                    pass
                else:
                    break
                #loop para provocar chute da palavra quando tiver somente 1 letra faltante ou 1 tentativa de erro faltante
                if contar_elementos(palavra_chute) == 1 or tentativas_erros == 1 and perg_chute.upper() == 'N':
                        print(f'** Suas tentativas erro ou espaço da palavra já estão praticamente preenchidos você precisa chutar qual é a palavra! {" ".join(palavra_chute)} **')
                        chute_final,retorno_chute2 = chutar_palavra('Y', palavra_secreta, palavra_chute)
                        pontos += retorno_chute2
                        break
            #condição para deduzir quantidade de tentativas restantes perde 5 pontos a cada erro de letra
            if not acertou_letra:
                tentativas_erros-=1
                pontos -=5
                print(f'Você tem {tentativas_erros} tentativas de erro restantes')

            # valida se as tentativas de errar letra foram zeradas para marcar como enforcou
            if tentativas_erros <= 0:
                enforcou = True
                pontos -=20
                print(f'Suas chances acabaram! a palavra era: {palavra_secreta}')

            # valida se a palavra secreta está igual a palavra chute depois de finalizar todos os chutes
            if palavra_secreta.upper() == "".join(palavra_chute).upper():
                acertou = True
                pontos += 20

                # Verifica se o resultado do chute é None (usuário não quer chutar)
                if resultado_perg_chute is None:
                    continue

                # Verifica se o chute foi bem-sucedido
                if not resultado_perg_chute:
                    continue



        except ValueError:
            print('Digite somente letras do alfabeto!')

    #premimo se acertar a palavra sem errar nenhuma letra de 50 pontos
    pontos += 50 if acertou and not letras_chute_incorreta else 0
    return pontos
    # aciona função para reiniciar o jogo caso seja apontado Y

#função que determina o nível do jgo se for facil acima a função que capta a lista de palavras e dificil usa api para pegar uma palavra aleatória
def nivel_jogo():
    while True:
        try:
          #recebe do usuário qual o nível de dificuldade que terá o jogo
            info_nivel = int(input('Digite o Nível do jogo (1 - Fácil, 2 - Difícil) : '))
            return info_nivel
        except ValueError:
            print('Digite somente um número inteiro')

#função que gera palavras de acordo com o nível
def determinar_palavras(nivel_do_jogo):
    if nivel_do_jogo == 1:
        while True:
            palavra_secreta = escolher_palavra()
            if palavra_secreta:
                significado = busca_palavra_secreta.obter_significado(palavra_secreta)
                sinonimos = busca_palavra_secreta.obter_sinonimos(palavra_secreta)
            if significado is not None and sinonimos is not None:
                break
    elif nivel_do_jogo == 2:
        while True:
            palavra_secreta = busca_palavra_secreta.palavra()
            if palavra_secreta:
                significado = busca_palavra_secreta.obter_significado(palavra_secreta)
                sinonimos = busca_palavra_secreta.obter_sinonimos(palavra_secreta)
            if significado is not None and sinonimos is not None:
                break
    # determinar significado e sinonimo da palavra:
    significado = busca_palavra_secreta.obter_significado(palavra_secreta)
    sinonimos = busca_palavra_secreta.obter_sinonimos(palavra_secreta)
    return palavra_secreta,significado,sinonimos

# função que faz validação qual jogador foi o vencedor
def gerenciamento_do_jogo():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

# loop para movimentar o jogo e também validar a quantidade de participantes
    while True:
        nivel_do_jogo = nivel_jogo()
        palavra_secreta1, significado1, sinonimos1 = determinar_palavras(nivel_do_jogo)
        try:
  # difine quantidade de participantes do jogo
            quant_jogadores = int(input('Quantos jogadores participação? 1 ou 2: '))
#valida si tiver somente 1 jogador para operar o jogo somente 1 uvez
            if quant_jogadores == 1:
                jogador1_pontos = jogar(palavra_secreta1,significado1,sinonimos1,nivel_do_jogo)
                print(f'você conquistou {jogador1_pontos} pontos')
                break
      #valida caso tenha 2 jogadores para dar a inicialização de do jogo para cada jogador e guarda os pontos somados
            elif quant_jogadores ==2:
                print('**** Inicia Jogo do jogador 1 **** \n')
                jogador1_pontos = jogar(palavra_secreta1,significado1,sinonimos1,nivel_do_jogo)
                print(f'Jogador 1 você conquistou {jogador1_pontos} pontos\n')
                print('**** Inicia Jogo do jogodador 2 **** \n')
                palavra_secreta2,significado2,sinonimos2 = determinar_palavras(nivel_do_jogo)
                jogador2_pontos = jogar(palavra_secreta2,significado2,sinonimos2,nivel_do_jogo)
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



if __name__ == "__main__":
    gerenciamento_do_jogo()
