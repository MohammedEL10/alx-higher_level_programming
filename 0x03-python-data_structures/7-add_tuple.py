#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple1 = [1, 89]
    tuple2 = [88, 11]
        tup=[]
    for i in range(0, len(tuple1)):
    tup.append(tuple1[i] + tuple2[i])
    result = tuple(tup)
