# -*- coding: utf-8 -*-
from random import randint
from utils import POS


def rand_price(range_ = (1, 70)):
    price = randint(*range_) * 10
    price += randint(0, 9)
    return price


class Property:
    def __init__(self, id_, rent_percent = 10, sale_price=None, rental_price=None):
        self.id_ = id_
        self._rent_percent = rent_percent
        if sale_price is not None and rental_price is not None:
            self.sale_price = sale_price
            self.rental_price = rental_price
        else:
            self._random_property()
            
        self._owner = None
        
    @property
    def owner(self, ):
        return self._owner
    
    
    def set_owner(self, player = None):
        self._owner = player
        

    def _random_property(self, ):
        self.sale_price = rand_price()
        self.rental_price = round(self.sale_price * self._rent_percent / 100)
        
    def can_be_purchased(self, player) -> POS:
        if self._owner is not None:
            if self._owner == player:
                return POS.OWNER
            return POS.ALREADY_OWNED
        return POS.AVAILABLE
        
    def __repr__(self, ):
        return f'<Property | {self._owner.name if self._owner else None} | ${self.sale_price} >'