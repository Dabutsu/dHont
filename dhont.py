# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:43:50 2019
D'hont simulator
@author: Dabutsu
"""
from itertools import chain
from csv import reader

def make_list(entry_list: list) -> list:
    temp = ["spam"]
    for i in range(1, len(entry_list)):
        temp.append([])
        for j in range(len(entry_list[0])):
            temp[i].append([entry_list[0][j], entry_list[i][j]])
    return temp
        
def scrap_parties(entry_list: list) -> dict:
    return {i[0]: int(i[1]) for i in entry_list}

def dhont(pop_dict: dict, poss_mandates: int) -> dict:
    def divided(number: int, n_operations: int, party_name: str) -> list:
        return [[party_name, number // i] for i in range(1, n_operations)]
    
    def process(parties: list) -> None:
        for i in range(poss_mandates):
            temp = max(parties, key=lambda x: x[1])
            results[temp[0]] += 1
            parties.remove(temp)

    results = {i:0 for i in list(pop_dict.keys())}
    process(list(chain.from_iterable([divided(pop_dict[i], 12, i) for i in list(pop_dict.keys())])))
    return scrap_parties(sorted(results.items(), key=lambda x: x[1], reverse=True))
    
def whole_country(areas: list, mandates: list) -> list: 
    return [dhont(scrap_parties(areas[i]), mandates[i]) for i in range(1, len(areas)-1)]


if __name__ == "__main__":
    with open("mandaty.txt") as numbers:
        n_mandates = [int(i.rstrip()) for i in numbers.readlines()]
        
    with open("wyniki.csv", newline='') as file:
        temp = [i[0].split(";") for i in reader(file, delimiter=" ")]
    
    result = whole_country(make_list(temp), n_mandates)
    
    print(result[23-1])
