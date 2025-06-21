''' Can a set contain tuples that themselves contain mutable elements (like lists)? If not, how can you modify such a tuple 
to make it hashable and storable in a set?
What happens if you try to create a set like this:
my_set = { (1, [2, 3]) }  
 '''


'my_set = { (1, [2, 3]) }' 
'''It shows error unhashable type: list because [2,3] is list which is unhashable and mutable but sets are hashable and immutable. 
So the set cannot store the list inside it. 
to make it hashable and storable in a set we need to make one more tuple inside the tuple.'''

my_set = {(1,(2,3))}
print(my_set)