# -*- coding: utf-8 -*-

from random import shuffle
from time import time
from uuid import uuid4

from .properties import Property


class Board:
    def __init__(self, spaces=20, players_list = [], rent_percent = 10):
        self.size = spaces
        self.players_list = players_list
        self.losers_list = []
        self.timeout = False
        self.winner = None
        self._rent_percent = rent_percent
        self._new_properties()
        self.stats = {}
   
        
        
    @property
    def game_order(self, ):
        return self._game_order
    
    
    def _new_properties(self, ):
        self.properties_ids_list = [str(uuid4()) for _ in range(self.size)]
        self.properties =  [Property(id_ = id, rent_percent=self._rent_percent) for id in self.properties_ids_list]
    
    
    def _more_rich(self, ):
        _max =  max(self._game_order, key= lambda item: item.balance)
        return _max
        
    def _reset_game(self, ):
        self.generate_stats()
        [player.reset() for player in self.players_list]
        self._new_properties()
        self.winner = None
        self.timeout = False
        
     
    def start(self, simulations = 300):
        init_time = time()
        for n in range(simulations):
            self.simulation = n
            game_order = self.players_list.copy()
            shuffle(game_order)
            
            [setattr(p, 'order', i) for i, p in enumerate(game_order)]
            
            self._game_order = game_order
            self.turns_count = 0
            while True:
                for player in self._game_order:
                    try:
                        result = player.play(self)
                        if result:
                            continue
                        self.losers_list.append(player)
                        self._game_order.remove(player)
                    except:
                        pass
                self.turns_count += 1
                
                if len(self._game_order) == 1:
                    self.winner = self._game_order[0]
                    break
                
                elif self.turns_count >= 1000:
                    self.timeout = True
                    self.winner = self._more_rich()
                    break
                   
            #print(self.winner, "VENCEU!!", f'| {self.turns_count}')
            self.turn_time = time() - init_time
            self._reset_game()
            
        return self.winner, self.turns_count
    
    
    def generate_stats(self, ):
        stats_dict = {
            f'{self.simulation}': {
                'timeout': self.timeout,
                'n_turns': self.turns_count,
                'winner': self.winner.name,
                'winner_behavior': self.winner._behavior,
                'properties_value_mean': sum(
                    [p.sale_price for p in self.properties]
                    )/ self.size,
                'rent_percent': self._rent_percent,
                'turn_time': self.turn_time
                }
            }
        self.stats.update(stats_dict)