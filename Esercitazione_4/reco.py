import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Hit:
    def __init__(self, a, b, c):
        self.id_modulo = a     
        self.id_sensore = b
        self.time_stamp = c
    def __lt__(self, other):
        if  self.time_stamp < other.time_stamp:
            return True
        elif self.time_stamp == other.time_stamp:
            if self.id_modulo < other.id_modulo:
                return True
            elif self.id_modulo == other.id_modulo:
                if self.id_sensore <= other.id_sensore:
                    return True
        return False
    def __gt__(self, other):
        if  self.time_stamp > other.time_stamp:
            return True
        elif self.time_stamp == other.time_stamp:
            if self.id_modulo > other.id_modulo:
                return True
            elif self.id_modulo == other.id_modulo:
                if self.id_sensore >= other.id_sensore:
                    return True
        return False
    def __add__(self, other):
        return self.time_stamp + other.time_stamp
    def __sub__(self, other):
        return self.time_stamp - other.time_stamp
