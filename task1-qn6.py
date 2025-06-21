'This loop runs infinitely. Why?'

x = 1.0
while x != 1.5:
    print(x)
    x += 0.1

    ''' the condition is always true as x never becomes exactly 1.5 because the computer reads 1.10000000000 like this something '''
