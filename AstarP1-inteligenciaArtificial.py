class Vertice: 
    def __init__(self, nome, distanciaObjetivo): #Função de inicialização
        self.nome = nome #Nome do Vértice(Local da UFMA)
        self.distanciaObjetivo = distanciaObjetivo #Distancia do Vértice até o objetivo
        self.visitado = False #Se o vértice já foi visitado
        self.adjacentes = [] #Vértices vizinhos
    
    def adicionaAdjacente(self, adjacente): #Função de adicionar adjacente(Vizinho)
        self.adjacentes.append(adjacente)

    def mostarAdjacente(self): #Percorre e printa os vértices adjacentes
        for i in self.adjacentes:
            print(i.vertice.nome, i.custo)

class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo #Custo até o objetivo em linha reta
        self.distanciaAestrela = vertice.distanciaObjetivo + self.custo #Formula da busca A*


class Grafo: #Grafo para organização dos lugares
  entradaUfma = Vertice('Entrada UFMA', 1340) #Atribuindo nome e distância ao objetivo
  oceano = Vertice('Prédio Oceanografia', 1335)
  farma = Vertice('Prédio Farmácia', 1090)
  sinfra = Vertice('SINFRA', 959)
  pFreire = Vertice('Paulo Freire', 576)
  ccso = Vertice('CCSO', 826)
  cebVelho = Vertice('CEB velho', 1030)
  ru = Vertice('RU', 802)
  ccet = Vertice('CCET', 613)
  edFis = Vertice('ED. Física', 478)
  planet = Vertice('Planetário', 574)
  empreend = Vertice('Empreendendorismo', 379)
  lago = Vertice('Lago UFMA', 187)
  bict = Vertice('Prédio BICT', 0)
 
  #Simulando o movimento de vértice a adjacente e o custo
  entradaUfma.adicionaAdjacente(Adjacente(oceano, 160))
  entradaUfma.adicionaAdjacente(Adjacente(sinfra, 500))
  
  oceano.adicionaAdjacente(Adjacente(entradaUfma, 160))
  oceano.adicionaAdjacente(Adjacente(farma, 450))

  farma.adicionaAdjacente(Adjacente(oceano, 160))
  farma.adicionaAdjacente(Adjacente(cebVelho, 350))

  sinfra.adicionaAdjacente(Adjacente(entradaUfma, 500))
  sinfra.adicionaAdjacente(Adjacente(pFreire, 450))
  

  pFreire.adicionaAdjacente(Adjacente(sinfra, 450))
  pFreire.adicionaAdjacente(Adjacente(ccso, 350))
  pFreire.adicionaAdjacente(Adjacente(edFis, 500))

  ccso.adicionaAdjacente(Adjacente(pFreire, 350))
  ccso.adicionaAdjacente(Adjacente(ru, 350))

  cebVelho.adicionaAdjacente(Adjacente(farma, 350))
  cebVelho.adicionaAdjacente(Adjacente(ru, 260))

  ru.adicionaAdjacente(Adjacente(cebVelho, 260))
  ru.adicionaAdjacente(Adjacente(ccso, 350))
  ru.adicionaAdjacente(Adjacente(ccet, 100))

  ccet.adicionaAdjacente(Adjacente(ru, 100))
  ccet.adicionaAdjacente(Adjacente(lago, 700))
  

  edFis.adicionaAdjacente(Adjacente(pFreire, 500))
  edFis.adicionaAdjacente(Adjacente(planet, 150))
  

  planet.adicionaAdjacente(Adjacente(edFis, 150))
  planet.adicionaAdjacente(Adjacente(empreend, 300))

  empreend.adicionaAdjacente(Adjacente(planet, 300))
  empreend.adicionaAdjacente(Adjacente(bict, 350))
  

  lago.adicionaAdjacente(Adjacente(ccet, 700))
  lago.adicionaAdjacente(Adjacente(bict, 280))

  bict.adicionaAdjacente(Adjacente(lago, 280))
  bict.adicionaAdjacente(Adjacente(empreend, 350))
  
grafo = Grafo()
    
import numpy as np
class VetorOrdenado: #Utilizando vetor ordenado para armazenar as cidades adjacente
  
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=object) # Mudança no tipo de dados, armazenando objetos

  # Referência para o vértice e comparação com a distância para o objetivo
  def insere(self, adjacente):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return
    posicao = 0
    for i in range(self.ultima_posicao + 1): #Percorre o vetor
      posicao = i
      if self.valores[i].distanciaAestrela > adjacente.distanciaAestrela: #Posição encontrada
        break
      if i == self.ultima_posicao: #Caso de atualizar ultima posição
        posicao = i + 1
    x = self.ultima_posicao
    while x >= posicao: #Faz o caminho da volta para inserir valores
      self.valores[x + 1] = self.valores[x] #Desloca valores
      x -= 1
    self.valores[posicao] = adjacente
    self.ultima_posicao += 1

  def imprime(self): #Função para imprimir resultado
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i].vertice.nome, ' : ', 
              self.valores[i].custo, "Custo", ' - ', 
              self.valores[i].vertice.distanciaObjetivo,"Distância para o objetivo", ' - ',
              self.valores[i].distanciaAestrela, "Distância estrela")

class AEstrela: #Implementação do A estrela
  
  def __init__(self, objetivo): #Objetivo inicializado como falso
    self.objetivo = objetivo
    self.encontrado = False

  def buscar(self, atual): #Testa se o vértice atual é objetivo
    print('------------------')
    print('Atual: {}'.format(atual.nome))
    atual.visitado = True #Marca o atual como visitado

    if atual == self.objetivo:
      self.encontrado = True
    else:
      vetor_ordenado = VetorOrdenado(len(atual.adjacentes)) #Cria-se um vetor
      for adjacente in atual.adjacentes: #Percorre a lista dos adjacentes ao vértice atual
        if adjacente.vertice.visitado == False: #Se o vértice atual não foi visitado
          adjacente.vertice.visitado = True #Agora é dado como visitado
          vetor_ordenado.insere(adjacente) #Inserido como vizinho 
      vetor_ordenado.imprime()

      if vetor_ordenado.valores[0] != None: #Se existir algo no indície 0
        self.buscar(vetor_ordenado.valores[0].vertice) #Busca sera feita novamente no indície 0, sendo um dos lugares da UFMA

busca_aestrela = AEstrela(grafo.bict) #Destino

busca_aestrela.buscar(grafo.entradaUfma) #Local de origem
