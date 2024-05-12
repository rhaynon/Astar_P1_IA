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
    

