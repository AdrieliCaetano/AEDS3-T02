from disciplina import Disciplina
from typing import List, Tuple

class Graph:
    def __init__(self, node_count: int = 0, edge_count: int = 0, adj_list: List[List[Tuple[int, int]]] = []) -> None:
        self.node_count = node_count
        self.edge_count = edge_count
        self.adj_list = adj_list
        if adj_list == []:
            for _ in range(self.node_count):
                self.adj_list.append([])

    def add_directed_edge(self, u: int, v: int, w: int):
        if u < 0 or u >= len(self.adj_list) or v < 0 or v >= len(self.adj_list):
            print(f"Node u={u} or v={v} is out of allowed range (0, {self.node_count - 1})")
        self.adj_list[u].append((v, w))
        self.edge_count += 1

    def add_undirected_edge(self, u: int, v: int, w: int):
        self.add_directed_edge(u, v, w)
        self.add_directed_edge(v, u, w)

    def convert_disc_in_graph(self, disc: List[Disciplina]):
        """Converte um lista de disciplinas em grafo, adicionando as arestas necessárias"""
        for i in range(self.node_count):
            if i < len(disc):
                if disc[i].dep == []:
                    self.add_directed_edge(0, disc[i].index,0)
                else:
                    for dp in disc[i].dep:
                        self.add_directed_edge(dp.index,disc[i].index, 1)
            if i != 0 and i != self.node_count-1:
                self.add_directed_edge(i,self.node_count-1,1)


    def bellman_ford_improved(self, s):
        """Bellman-Ford adaptado para encontrar o caminho crítico (máximo)"""
        dist = [float("-inf")] * self.node_count
        pred = [-1] * self.node_count
        dist[s] = 0
        for i in range(self.node_count - 1):
            swapped = False
            for u in range(len(self.adj_list)):
                for (v, w) in self.adj_list[u]:
                    if dist[v] < dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                        swapped = True
            if not swapped:
                break
        return (dist, pred)
    
def rec_path(s, t,pred):
    """Recupera o camínho máximo a partir dos predecessores gerados no Bellman-Ford"""
    C = [t]
    aux = t
    while aux != s:
        aux = pred[aux]
        C.insert(0, aux)
    return C
