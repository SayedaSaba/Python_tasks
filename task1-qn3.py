'What happens if you modify the loop variable inside a for loop?'

for i in range(5):
    print(i)
    if i == 2:
        i += 1

        '''The loop gives values from range(5), Even if we change i inside the loop, Python doesnot see it or ignores it.
         The loop still follows the original numbers and the output remains the same'''
