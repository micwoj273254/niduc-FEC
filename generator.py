import numpy as np
import random

def generate_bits(quantity):
    return [random.randint(0,1) for i in range(0, quantity)]
    #quantity - amount of bits to generate