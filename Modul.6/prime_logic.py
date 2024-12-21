import collections
if not hasattr(collections, 'Iterator'):
    from collections.abc import Iterator
    collections.Iterator = Iterator

    import collections
if not hasattr(collections, 'Hashable'):
    from collections.abc import Hashable
    collections.Hashable = Hashable
    
from kanren import isvar, run, membero
from kanren.core import success, fail, condeseq, eq, var
from sympy.ntheory.generate import prime, isprime
import itertools as it

def prime_check(x):
    # Check if x is a variable; if yes, generate prime numbers
    if isvar(x):
        return condeseq([(eq, x, p)] for p in map(prime, it.count(1)))
    else:
        # If x is a value, check if it's prime
        return success if isprime(x) else fail

# Define a logical variable
x = var()

# Define the dataset
data = (12, 14, 15, 19, 20, 21, 22, 23, 29, 30, 41, 44, 52, 62, 65, 85)
print("Data:", data)

# Find primes in the dataset
var_x = membero(x, data)
member = run(0, x, var_x, prime_check(x))
fn = set(member)
print("Berikut adalah bilangan prima yang ada di dalam data:", fn)

# Generate the first 10 prime numbers
ten_prime = run(10, x, prime_check(x))
print("Sepuluh bilangan prima pertama:", ten_prime)
