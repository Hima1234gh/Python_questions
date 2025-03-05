# To generate pseudo random numbers.

a = 1664525
c = 1013904223
m = 2**32

def pseudo_random(seed):
    return ((a*seed+c) % m)



seed = int(input("Enter a Number : "))

new_seed = pseudo_random(seed)
print(new_seed)