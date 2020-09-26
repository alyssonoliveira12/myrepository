import numpy as np
import queue as q


def cria_labirinto():

    # variaveis da classe

    matriz_labirinto = []

    for i in range(10):

        linha = []

        for j in range(10):

            linha.append(0)

        matriz_labirinto.append(linha)

    matriz_labirinto[0][0] = 2
    matriz_labirinto[4][0] = 3
    for i in range(1, 4):
        matriz_labirinto[i][0] = 1
    for i in range(1, 8):
        matriz_labirinto[3][i] = 1
    for i in range(3,7):
        matriz_labirinto[i][4] = 1
    for i in range(4, 10):
        matriz_labirinto[i][7] = 1
    for i in range(5, 7):
        matriz_labirinto[9][i] = 1
   # for i in range(2, 6):
     #   matriz_labirinto[6][i] = 0
    #for i in range(5, 7):
       # matriz_labirinto[9][i] = 1

    return matriz_labirinto

def imprime_matriz(matriz):

    print(np.matrix(matriz))

    print('\n')

    return

class Agente:

    # Construtor
    def __init__(self, maze):

        #Valor que representa o agente
        self.valor_agente = 2
        #Valor que representa o objetivo
        self.valor_objetivo = 3

        # Posição atual do Agente  na  matriz labirinto, onde x = linha e y = coluna
        self.posicao_atual_x = 0
        self.posicao_atual_y = 0
        self.localiza_agente()

        # Posição do objetivo  na  matriz labirinto, onde x = linha e y = coluna
        self.posicao_objetivo_y = 0
        self.posicao_objetivo_x = 0
        self.localiza_objetivo()

        #Labirinto que o agente terá que percorrer
        self.labirinto = maze

        #Cria uma matriz para colocar o valor dos custos
        self.matriz_de_custos = []
        self.inicializa_matriz_de_custos()

        #listas com as posicoes visitadas
        self.lista_visitados_x = []
        self.lista_visitados_y = []

        self.fila_tmp = q.PriorityQueue()
        self.usando_fila_tmp = False
        self.caminho_final = q.Queue()

        self.entrada_bifurcacao_x = 0
        self.entrada_bifurcacao_y = 0

    #Função que localiza a posição atual do agente
    def localiza_agente(self):

        for i in range(10):

            for j in range(10):

                if self.labirinto[i][j] == 2:

                    self.posicao_atual_x = i
                    self.posicao_atual_y = j

                    print("Agente esta na posicao", self.posicao_atual_x,self.posicao_atual_y)

                    return

    # Função que localiza a posição atual do agente -- NÃO PRECISA
    def localiza_objetivo(self):

        for i in range(10):

            for j in range(10):

                if self.labirinto[i][j] == 3:

                    self.posicao_objetivo_x = i
                    self.posicao_objetivo_y = j

                    print("Objetivo esta na posicao", self.posicao_objetivo_x, self.posicao_objetivo_y)

                    return

    def inicializa_matriz_de_custos(self):

        for i in range(10):

            linha = []

            for j in range(10):
                linha.append(0)

            self.matriz_de_custos.append(linha)

    #Funções para movimentar o agente
    def andar_para_direita(self):

        #verifica se esta dentro dos limites da matriz

        if self.posicao_atual_y == 9:
            print("Cuidado! Vcê atingiu o limite do labirinto")
            return False

        else:
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 1
            self.posicao_atual_y = self.posicao_atual_y + 1
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 2



            print("andou para direita")
            print("Labirinto Estado Atual")
            imprime_matriz(self.labirinto)
            return True
    def andar_para_esquerda(self):

        # verifica se esta dentro dos limites da matriz
        if self.posicao_atual_y == 0:
            print("Cuidado! Vcê atingiu o limite do labirinto")
            return False

        else:
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 1
            self.posicao_atual_y = self.posicao_atual_y - 1
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 2
            print("andou para esquerda")
            print("Labirinto Estado Atual")
            imprime_matriz(self.labirinto)
            return True
    def andar_para_cima(self):

        if self.posicao_atual_x == 0:
            print("Cuidado! Vcê atingiu o limite do labirinto")
            return False

        else:
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 1
            self.posicao_atual_x = self.posicao_atual_x - 1
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 2

            print("andou para cima")
            print("Labirinto Estado Atual")
            imprime_matriz(self.labirinto)
            return True
    def andar_para_baixo(self):

        if self.posicao_atual_x == 9:
            print("Cuidado! Vcê atingiu o limite do labirinto")
            return False

        else:
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 1
            self.posicao_atual_x = self.posicao_atual_x + 1
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 2

            print("andou para baixo")
            print("Labirinto Estado Atual")
            imprime_matriz(self.labirinto)
            return True

    #Funções para verificar se os espaços estão livres ou não paredes
    def verifica_direita(self):
        if self.posicao_atual_y == 9:
            #print("Cuidado! Vcê atingiu o limite do labirinto")
            return False
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y + 1] == 1:
            #print("Pode andar para direita")
            return 1
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y + 1] == 3:
            #print("Você chegou no Objetivo! Parabéns")
            return 3
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y + 1] == 0:
            #print("OPS! Parede")
            return 0
    def verifica_esquerda(self):
        if self.posicao_atual_y == 0:
            #print("Cuidado! Vcê atingiu o limite do labirinto")
            return False
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y - 1] == 1:
            #print("Pode andar para esquerda")
            return 1
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y - 1] == 3:
            #print("Você chegou no Objetivo! Parabéns")
            return 3
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y - 1] == 0:
            #print("OPS! Parede")
            return
    def verifica_em_cima(self):
        if self.posicao_atual_x == 0:
            #print("Cuidado! Vcê atingiu o limite do labirinto")
            return False
        if self.labirinto[self.posicao_atual_x - 1][self.posicao_atual_y] == 1:
            #print("Pode andar para cima")
            return 1
        if self.labirinto[self.posicao_atual_x - 1][self.posicao_atual_y] == 3:
            #print("Você chegou no Objetivo! Parabéns")
            return 3
        if self.labirinto[self.posicao_atual_x -1][self.posicao_atual_y] == 0:
            #print("OPS! Parede")
            return 0
    def verifica_em_baixo(self):
        if self.posicao_atual_x == 9:
            #print("Cuidado! Vcê atingiu o limite do labirinto")
            return False
        if self.labirinto[self.posicao_atual_x + 1][self.posicao_atual_y] == 1:
            #print("Pode andar para baixo")
            return 1
        if self.labirinto[self.posicao_atual_x + 1][self.posicao_atual_y] == 3:
            #print("Você chegou no Objetivo! Parabéns")
            return 3
        if self.labirinto[self.posicao_atual_x +1][self.posicao_atual_y] == 0:
            #print("OPS! Parede")
            return 0

    def ja_visitou(self,x,y):

        for i in range(len(self.lista_visitados_x)):

            if self.lista_visitados_x[i] == x and self.lista_visitados_y[i] == y:
                print("já Visitou esse lugar, procure outro!")
                return True

        self.lista_visitados_x.append(x)
        self.lista_visitados_y.append(y)

        return False

    def calcula_heuristica(self, x, y):

        distancia_x = abs(self.posicao_objetivo_x - x)

        distancia_y = abs(self.posicao_objetivo_y - y)

        distancia_heuristica = distancia_x + distancia_y

        return distancia_heuristica

    def calcula_custo_total(self):

        #custo_uniforme = 0

        for i in range(10):

            for j in range(10):

                if self.labirinto[i][j] == 1:

                    custo_heuristico = self.calcula_heuristica(i, j)

                    # custo_uniforme = custo_uniforme + 1

                    self.matriz_de_custos[i][j] = custo_heuristico #+ custo_uniforme

        print("Matriz de custo")

        imprime_matriz(self.matriz_de_custos)

        return

    def verifica_numero_de_escolha(self):

        n_escolhas = 0

        if (self.verifica_direita() == 1):

            n_escolhas += 1

        if (self.verifica_em_baixo() == 1):

            n_escolhas += 1

        if (self.verifica_esquerda() == 1):

            n_escolhas += 1

        if (self.verifica_em_cima() == 1):

            n_escolhas += 1

        return n_escolhas

#Nessa função ele utiliza as funções de verificação. Primeiro ele verifica a direita se o caminho estiver livre ele verifica a matriz de custos
#e atribui o variável maior e decisao = 1. Se esquerda estiver livre e o valor da matriz de custos for maior que a variável  maior
#ele atualiza menor e muda a decisão. a função repete o mesmo procedimento para cima e para baixo.
#O valor da decisao final, a quem tem o menor valor de custo será o quadrado que o agente irá se movimentar.
#O movimento será feito pela chamada da função movimento
#decisao = 1 move para direita
# decisao = 2 move para esquerda
# decisao = 3 move para emcima
# decisao = 4 move para baixo
    def resultado(self):

        menor = 0
        decisao = 0

        n_escolhas = self.verifica_numero_de_escolha()

        heuristica_cima = self.calcula_heuristica(self.posicao_atual_x - 1,self.posicao_atual_y)
        heuristica_baixo = self.calcula_heuristica(self.posicao_atual_x + 1,self.posicao_atual_y)
        heuristica_esquerda = self.calcula_heuristica(self.posicao_atual_x,self.posicao_atual_y - 1)
        heuristica_direita = self.calcula_heuristica(self.posicao_atual_x,self.posicao_atual_y + 1)

        if n_escolhas == 1 and not self.usando_fila_tmp:
            self.usando_fila_tmp = False

        #ENTREI NUMA BIFURCACAO

        if n_escolhas > 1:
            self.usando_fila_tmp = True
            self.entrada_bifurcacao_y = self.posicao_atual_y
            self.entrada_bifurcacao_x = self.posicao_atual_x

        if (self.verifica_direita() == 1 and self.ja_visitou(self.posicao_atual_x,self.posicao_atual_y + 1) == False) or self.verifica_direita() == 3:

            menor = heuristica_direita
            decisao = 1

        if (self.verifica_esquerda() == 1 and self.ja_visitou(self.posicao_atual_x, self.posicao_atual_y - 1) == False) or self.verifica_esquerda() == 3:

           if heuristica_esquerda < menor or menor == 0:

                menor = heuristica_esquerda
                decisao = 2

        if (self.verifica_em_cima() == 1 and self.ja_visitou(self.posicao_atual_x - 1, self.posicao_atual_y) == False) or self.verifica_em_cima() == 3:

            if heuristica_cima < menor or menor == 0:

                menor = heuristica_cima
                decisao = 3

        if (self.verifica_em_baixo() == 1 and self.ja_visitou(self.posicao_atual_x + 1, self.posicao_atual_y) == False) or self.verifica_em_baixo() == 3:

            if heuristica_baixo < menor or menor == 0:

                menor = heuristica_baixo
                decisao = 4


        if not self.usando_fila_tmp:

            self.caminho_final.put(decisao)

        if self.usando_fila_tmp:
            #Se nao tiver mais saida
            if n_escolhas == 0:

                self.posicao_atual_x = self.entrada_bifurcacao_x
                self.posical_atual_y = self.entrada_bifurcacao_y
                self.fila_tmp.get() #TIRA A ENTRADA DA LISTA, ELA FICA COMO CELULA VISITADA

                if self.fila_tmp.empty():
                    self.usando_fila_tmp = False

        print(decisao)
        self.movimenta(decisao)

    def movimenta(self, decisao):
        if decisao == 1:
            print()
            self.andar_para_direita()
        if decisao == 2:
            self.andar_para_esquerda()
        if decisao == 3:
            self.andar_para_cima()
        if decisao == 4:
            self.andar_para_baixo()

 #   def objetivo(self):
 #       if self.posicao_atual_x == self.posicao_objetivo_x and self.posicao_atual_y == self.posicao_objetivo_y:
 #           return True
 #       else:
 #           return False
    def busca_A(self,resultado):

        max_iteracoes = 100

        contador = 0

        if contador == max_iteracoes:
            return ValueError
        else:
            contador = contador + 1

            ##ARRUMAR ISSO PRA DAR ULTIMO PASSO
        #if self.verifica_direita() == 3 or self.verifica_esquerda() == 3 or self.verifica_em_cima() == 3 or self.verifica_em_baixo() == 3:
        if self.posicao_atual_y == self.posicao_objetivo_y and self.posicao_atual_x == self.posicao_objetivo_x:

            print("Você saiu do labirinto")
            return

        else:
            return self.busca_A(self.resultado())
