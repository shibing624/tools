# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""

from matplotlib import pyplot as plt
import networkx as nx
g=nx.Graph()
g.add_nodes_from([1,2,3])
g.add_edges_from([(1,2),(1,3)])
nx.draw_networkx(g)
plt.show()
