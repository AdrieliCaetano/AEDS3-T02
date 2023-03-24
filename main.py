import pandas as pd
from disciplina import*
from graph import *

print("Informe o arquivo (0 para sair): ")
file_name = input()

if file_name == '0':
    print("Encerrando...")
else:
    print("\nProcessando...")
    data = pd.read_csv(file_name, dtype=str)
    disc = convert_df_in_disc(data)
    g1 = Graph(data.shape[0] + 2) # +2 = nós s e t 
    g1.convert_disc_in_graph(disc=disc)
    #print(g1.adj_list)
    #print_disc(disc)
    dist, pred = g1.bellman_ford_improved(0)
    C = rec_path(0, g1.node_count-1, pred)
    print("\nCaminho Crítico: ")
    print_disc_path(C, disc)
    print(f"\nTempo Mínimo: {dist[g1.node_count-1]}")



