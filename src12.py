var_set_a = set([1,2,4,6,7,8,9,10,11,14,16,18,19,20])
var_set_b = set([1,3,4,5,6,7,9,10,12,13,14,15,16,19,20])

print(var_set_a)
print(type(var_set_b))

var_set_a.add(21)

var_set_b.remove(20)
var_set_b.discard(20)

print(var_set_a - var_set_b)
print(var_set_a | var_set_b)
print(var_set_a & var_set_b)

print(var_set_a.union(var_set_b))
print(var_set_b.intersection(var_set_a))
print(var_set_a.difference(var_set_b))