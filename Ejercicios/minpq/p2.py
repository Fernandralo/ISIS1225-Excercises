import config

from DISClib.ADT import minpq as pq

"""
Encontrar las 5 noticias mas recientes
"""

def greater(key1, key2):
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1


minpq = pq.newMinPQ(greater)





