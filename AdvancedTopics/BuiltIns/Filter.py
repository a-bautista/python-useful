def less_than_ten(x):
    return x < 10

my_list = [1, 2, 3, 10, 11, 12]
for item in filter(less_than_ten, my_list):
    print(item)

for item in my_list:
    less_than_ten(item)

'''
    Take a function and an iterable, apply the function to the iterable. 
'''