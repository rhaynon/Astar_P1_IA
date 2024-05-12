from platform import node

import matplotlib.pyplot as plt
import networkx as nx

P = nx.Graph()

P.add_node('A', location='ENTRADA UFMA')
P.add_node('B', location='SINFRA')
P.add_node('C', location='PREDIO OCEANOGRAFIA')
P.add_node('D', location='PREDIO FARMACIA')
P.add_node('E', location='CEB VELHO')
P.add_node('F', location='RU')
P.add_node('G', location='CCSO')
P.add_node('H', location='CCET')
P.add_node('I', location='PAULO FREIRE')
P.add_node('J', location='PREDIO ED FIS')
P.add_node('K', location='PLANETARIO')
P.add_node('L', location='EMPREENDEDORISMO')
P.add_node('M', location='LAGO UFMA')
P.add_node('N', location='BICT')


P.add_edge('A','B', weight= 500)
P.add_edge('A','C', weight= 160)
P.add_edge('C','D', weight= 450)
P.add_edge('D','E', weight= 350)
P.add_edge('E','F', weight= 260)
P.add_edge('F','G', weight= 350)
P.add_edge('F','H', weight= 100)
P.add_edge('B','I', weight= 450)
P.add_edge('G','I', weight= 350)
P.add_edge('I','J', weight= 500)
P.add_edge('J','K', weight= 150)
P.add_edge('K','L', weight= 300)
P.add_edge('H','M', weight= 700)
P.add_edge('L','N', weight= 350)
P.add_edge('M','N', weight= 280)

pos={
    'A':(2,10),
    'B':(-3,10),
    'C':(2,8.4),
    'D':(-0.7,4.8),
    'E':(-4.2,4.8),
    'F':(-4.2,2.2),
    'G':(-6,6),
    'H':(-4.2,0.7),
    'I':(-7.4,10),
    'J':(-12.4,10),
    'K':(-13.5,8.9),
    'L':(-13.5,5.9),
    'M':(-11.5,0.3),
    'N':(-13.5,2.3)
}

pos_node_attributes={
    'A':(1.9,10.6),
    'B':(-3,10.6),
    'C':(3.83,8.41),
    'D':(0.8,4.8),
    'E':(-4.2,5.35),
    'F':(-3.6,2.2),
    'G':(-6.7,5.97),
    'H':(-3.5,0.7),
    'I':(-7.4,10.6),
    'J':(-12.4,10.6),
    'K':(-14.6,8.9),
    'L':(-15.2,5.9),
    'M':(-11.5,-0.28),
    'N':(-14.15,2.31)
}

node_labels={n:(d['location']) for n,d in P.nodes(data=True)}

edge_labels={(u,v):d['weight'] for u,v,d in P.edges(data=True)}

nx.draw(P,pos=pos, with_labels=True, node_color='blue', node_size=1000, font_color='White', font_size=10, font_weight='bold', width=3)
nx.draw_networkx_labels(P, pos=pos_node_attributes, labels=node_labels, font_color='black', font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(P, pos=pos, edge_labels=edge_labels, label_pos=0.5)
plt.margins(0.2)
plt.show()