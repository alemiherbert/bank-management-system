from random import seed, random
from math import floor


def gen_anum(b_id, a_id):
    seed(a_id)
    return b_id + str(floor(random()*1000)).rjust(5, '0')

