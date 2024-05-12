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
    

