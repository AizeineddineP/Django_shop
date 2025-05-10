import random
import time
from functools import lru_cache
CACHE_DICT ={}
from time import sleep

@lru_cache
def view_product(product:str)->None:
    if product not in CACHE_DICT:
       time.sleep(5)
       CACHE_DICT[product] = product
    print(CACHE_DICT[product])

products = [52,6,2,1,5]

for i in range(10):
    product = random.choice(products)
    view_product(product)