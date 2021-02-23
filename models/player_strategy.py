#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 03:20:32 2021

@author: pablolbispo
"""
from random import getrandbits

def impulsivo(curr_balance, property_):
    return True



def exigente(curr_balance, property_):
    return True if property_.rental_price > 50 else False



def cauteloso(curr_balance, property_):
    return True if (
        curr_balance - property_.sale_price
        ) > 80 else False


def aleatorio(curr_balance, property_):
    return bool(getrandbits(1))