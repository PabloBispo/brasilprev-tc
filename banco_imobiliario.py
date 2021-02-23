#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 16:38:47 2021

@author: pablolbispo
"""

from models.player import players_list
from models.board import Board
import pandas as pd


def run_game(simulations = 300, rent_percent = 10):
    board = Board(rent_percent=rent_percent)
    board.players_list = players_list
    
    winner, turns = board.start(simulations = simulations)
    
    stats = board.stats
    
    return stats


def show_stats(stats):
    df_stats = pd.DataFrame(stats.values())
    print(f'Partidas terminadas por timeout: {(df_stats.timeout == True).sum()}')
    print(f'Duração média das partidas: {round(df_stats.n_turns.mean())} turnos')
    behavior_count = df_stats.winner_behavior.value_counts()
    shape = df_stats.shape
    print("Porcentagem de vitórias por comportamento: ")
    for p in players_list:
        behavior = p._behavior
        percent = round(behavior_count.get(behavior, 0)/shape[0] * 100)
        print(f'\t {behavior.capitalize()} -> {percent}%')
    print(f'O comportamento que mais vence é o {behavior_count.index[0].capitalize()}')
    

