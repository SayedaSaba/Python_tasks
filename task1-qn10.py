'Given a list l = [10, 20, 30, 40, 50], write a program that removes the middle element (or elements if the length is even).'


l = [10, 20, 30, 40, 50 ]  

length = len(l)
middle = length // 2

if length % 2 == 1:
    midvalue = l[middle]
    l.remove(midvalue)
else:
    midvalue1 = l[middle]
    midvalue2 = l[middle - 1]
    l.remove(midvalue1)
    l.remove(midvalue2)

print(l)

