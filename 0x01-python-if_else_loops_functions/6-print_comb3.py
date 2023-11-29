#!/usr/bin/python3
def comb(L)
a=int(input("enter first number"))
b=int(input("enter second number"))

L.append(a)
L.append(b)

for a in range(2):
for b in range(2):

    print(L[a],L[b])
