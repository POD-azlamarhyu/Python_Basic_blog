type_list_prime = []

type_list_prime = [2,3,5,7,11,13,17,19]

print(type_list_prime)

print(type_list_prime[0])
print(type_list_prime[3])

for number in type_list_prime:
     print(number)

for i,number in enumerate(type_list_prime):
     print("{} : {}".format(i,number))

for i in range(len(type_list_prime)):
     print(type_list_prime[i])

type_list_prime.append(23)
type_list_prime.append(37)

type_list_prime.insert(9, 29)
type_list_prime.sort()
type_list_prime.remove(2)

alter_tuple = tuple(type_list_prime)

print(type(alter_tuple))