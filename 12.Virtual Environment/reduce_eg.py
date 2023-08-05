from functools import reduce


fun = lambda a,b : max(a,b)

l = [1,3,45,76,78,545,67,677,2,3,]

val = reduce(fun,l)
print(val)