from kanren import *
from kanren.core import lall
import collections
if not hasattr(collections, 'Iterator'):
    from collections.abc import Iterator
    collections.Iterator = Iterator
    
    import collections
if not hasattr(collections, 'Hashable'):
    from collections.abc import Hashable
    collections.Hashable = Hashable


from kanren import *
from kanren.core import lall

def left(q,p,list_data):
    return membero((q,p), zip(list_data,list_data[1:]))
def next(q,p,list_data):
    return conde( [left(q,p,list_data)],[left(p,q,list_data)])

houses = var()
 
rules_zebraproblem = lall(
    (eq, (var(), var(), var(), var(), var()), houses),
    (membero, ('Englishman', var(), var(), var(), 'red'), houses),
    (membero, ('Swede', var(), var(), 'dog', var()), houses),
    (membero, ('Dane', var(), 'tea', var(), var()), houses),
    (left, (var(), var(), var(), var(), 'green'), (var(), var(), var(), var(), 'white'), houses),
    (membero, (var(), var(), 'coffee', var(), 'green'), houses),
    (membero, ('Pall Mall', var(), var(), 'birds', var()), houses),
    (membero, (var(), 'Dunhill', var(), var(), 'yellow'), houses),
    (eq, (var(), var(), (var(), var(), 'milk', var(), var())), houses),
    (eq, (('Norwegian', var(), var(), var(), var()), var(), var(), var(), var()), houses),
    (next, (var(), 'Blend', var(), var(), var()), (var(), var(), var(), 'cats', var()), houses),
    (next, (var(), 'Dunhill', var(), var(), var()), (var(), var(), var(), 'horse', var()), houses),
    (membero, (var(), 'Blue Master', 'beer', var(), var()), houses),
    (membero, ('German', 'Prince', var(), var(), var()), houses),
    (next, ('Norwegian', var(), var(), var(), var()), (var(), var(), var(), var(), 'blue'), houses),
    (next, (var(), 'Blend', var(), var(), var()), (var(), var(), 'water', var(), var()), houses),
    (membero, (var(), var(), var(), var(), 'zebra'), houses)
)
solutions = run(0, houses, rules_zebraproblem)

val = input("enter your value ")
print(val)
output = [house for house in solutions[0] if val in house] [0] [0]
print('\n' + output + 'owns', val)
