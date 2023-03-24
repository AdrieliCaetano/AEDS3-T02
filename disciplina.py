import pandas as pd
from typing import List

class Disciplina:

    def __init__(self, index:int, cod: str, nome: str, per: int, dur: int) -> None:
        self.index = index
        self.cod = cod
        self.nome = nome
        self.per = per
        self.dur = dur
        self.dep: list[Disciplina] = []


def convert_df_in_disc(data):
    """Converte o DataFrame gerado pelo pandas em uma lista de disciplinas"""
    dep_list = []
    disc = []
    cod = data['Código']
    nome = data['Nome']
    per = data['Período']
    dur = data['Duração']
    for i, row in data.iterrows():
        dep = row['Dependências']
        discAux = Disciplina(i+1, cod[i], nome[i], per[i], dur[i])
        dep_list.append(str(dep).split(';'))
        disc.append(discAux)
    for i in range(data.shape[0]):
        for dp in dep_list[i]:
            for dc in disc:
                if dp == dc.cod:
                    disc[i].dep.append(dc)
    return disc


def print_disc(disc):
    """Imprime os dados de cada disciplina de uma lista de disciplinas"""
    for i in disc:
        print(i.index, end=",")
        print(i.cod, end=",")
        print(i.nome, end=",")
        print(i.per, end=",")
        print(i.dur, end=",")
        for j in range(len(i.dep)):
            print(i.dep[j].cod, end=" ")
        print('\n')

def print_disc_path(C, disc):
    """Imprime o nome da disciplina correspondente a cada nó (índice) no caminho C"""
    for c in C:
        for i in range(len(disc)):
            if disc[i].index == c:
                print(f"- {disc[i].nome}")




    
        

