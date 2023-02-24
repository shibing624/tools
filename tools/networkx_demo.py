# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import networkx as nx

# 节点
G = nx.Graph()
G.add_nodes_from([2,3])
G.add_nodes_from(range(100,110))
print(G.graph)
print(G.is_directed())
print(G.nodes)


G.add_node(1, time='spam')
G.add_nodes_from([3], time='2pm')
print(G.nodes[1])
print(G.nodes)

# edge 边
G.add_edge(2,3)
G.add_edges_from([(100,101), (101,102)])
print(G.edges)
print(G.graph)
print(len(G))
print(G.number_of_edges())
print(G.number_of_nodes())

# 图
G = nx.Graph(day='monday')
G.add_nodes_from([2,3])
G.add_nodes_from(range(100,110))
print(G.graph)

red = nx.random_lobster(100, 0.9, 0.9)
print(red)

import matplotlib.pyplot as plt
G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
plt.show()

options = {
    'node_color': 'black',
    'node_size': 100,
    'width': 3,
}
subax1 = plt.subplot(221)
nx.draw_random(G, **options)
subax2 = plt.subplot(222)
nx.draw_circular(G, **options)
subax3 = plt.subplot(223)
nx.draw_spectral(G, **options)
subax4 = plt.subplot(224)
nx.draw_shell(G, nlist=[range(5,10), range(5)], **options)
plt.show()