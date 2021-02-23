# -*- coding: utf-8 -*-

from enum import Enum
from random import randint

class POS(Enum):
    # Property Owning Status
    AVAILABLE = 1
    OWNER = 2
    ALREADY_OWNED = 3
    

class Dice:
    def __init__(self, sides=6):
        self._sides = sides
    
    
    def roll(self, ):
        return randint(1, self._sides)



def simple_walk(curr_position, spaces, board_size):
    assert curr_position < board_size, 'Posição inválida'
    final_pos = curr_position + spaces
    return final_pos if (
        final_pos < board_size
        ) else (
            final_pos - board_size
            )
