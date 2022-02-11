var = 10
source = 'var * 2'
source2 = "print('123')" 
print(eval(source))
print(eval(source2))

'''
    You indicate to evaluate the string expression source which contains a variable.
    The second expression is actually executing the print which is in a string.
'''