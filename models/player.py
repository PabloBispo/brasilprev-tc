# -*- coding: utf-8 -*-
from uuid import uuid4
from .properties import Property
from utils import POS, simple_walk, Dice


from .player_strategy import (
    impulsivo,
    exigente,
    cauteloso,
    aleatorio,
    )

    
dice = Dice()


class Player():
    def __init__(self, name, buy_behavior = None):
        self._name = name
        self._balance = 300
        self._properties = []
        self.id = f'player-{str(uuid4())[:8]}'
        self._position = 0
        self._lose = False
        self._buy_behavior = buy_behavior
        self.order = None
        self._behavior = self.name.split("_")[1]
        
    @property        
    def balance(self, ):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        self._balance = value
        if self._balance <= 0:
            self._end_game()
            
    @property
    def properties(self, ):
        return self._properties
           
    
    @property
    def name(self, ):
        return self._name
    
    @property
    def position(self, ):
        self._position
    
    @position.setter
    def position(self, value):
        self._position = value
        
        
    def increase_balance(self, amount:int):
        if amount >= 0:
            self._balance += amount
            
            
    def reset(self, ):
        self._balance = 300
        self._properties = []
        self._position = 0
        self._lose = False
        self.order = None
        
    
    def decrease_balance(self, amount:int, simulated:bool = False):
        ''' Valor que sera debitado da conta'''
        abs_amount = abs(amount)
        final_balance = self._balance - abs_amount
        if final_balance >= 0:
            if not simulated:
                self.balance = final_balance
            return True, self._balance
        else:
            return False, final_balance
    
    def will_buy(self, property_:Property):
        if self.decrease_balance(property_.sale_price, simulated=True)[0]:
            return self._buy_behavior(self._balance, property_)
        return False
    
    
    def pay_rent(self, other, property_):
        curr_balance = self._balance
        rental_price = property_.rental_price
    
        can_pay, rest = self.decrease_balance(rental_price)
        if not can_pay:
            self.decrease_balance(curr_balance)
        
        other.increase_balance(rental_price if can_pay else curr_balance)
        #print(self, 'paying rent')
        
    
    def buy(self, property_: Property):
        pos = property_.can_be_purchased(self, )
        if  pos == POS.ALREADY_OWNED:
            self.pay_rent(property_.owner, property_)
        elif pos == POS.OWNER:
            #print("Já comprada.")
            return
        else:
            # if pos.AVAILABLE
            if not self.will_buy(property_):
                #print('Saldo insuficiente.')
                return
            self.decrease_balance(property_.sale_price)
            property_.set_owner(self)
            self._properties.append(property_)
            #print("Comprado com sucesso!")
            
    def _walk(self, spaces, board_size):
        self._position = simple_walk(
            self._position, spaces, board_size
            )
            
    def play(self, board):
        spaces = dice.roll()
        self._walk(spaces, board.size)
        self.buy(board.properties[self._position])
        return False if self._lose else True
        
        
    def _return_properties(self, ):
        for prop in self._properties:
            prop.set_owner(None)
        self._properties.clear()
            
            
    def _end_game(self, ):
        self._return_properties()
        self._lose = True

            
    def __repr__(self, ):
        return f'<Player | {self._name} | ${self._balance} >'
    
    

player_impulsivo = Player(
    	'player_impulsivo',
    	 buy_behavior = impulsivo)
    	 
player_exigente = Player(
	'player_exigente',
	 buy_behavior = exigente)
	 
player_cauteloso = Player(
	'player_cauteloso',
	 buy_behavior = cauteloso)
	 
player_aleatorio = Player(
	'player_aleatorio',
	 buy_behavior = aleatorio)  

players_list = [
        player_impulsivo,
        player_exigente,
        player_cauteloso,
        player_aleatorio
        ]   
    