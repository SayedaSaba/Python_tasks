'''Without using slicing ([::-1]) or the reverse() method, reverse the list l = [5, 6, 7, 8, 9] using a loop or logic.'''

l = [5, 6, 7, 8, 9]
reversed_list = []
for i in range(len(l)-1,-1,-1):
    reversed_list.append(l[i])

    
print(reversed_list)