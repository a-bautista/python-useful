from collections import Counter

def count():
    # print(Counter('superfluous'))
    counter = Counter('superfluous')
    print(counter)
    print(counter.most_common(2))
    print(list(counter.elements()))
    print(counter['u'])

    print('*'*40)
    counter_one = Counter('superfluous')
    counter_two = Counter('Super') # it's not going to work
    counter_one.subtract(counter_two)
    print(counter_one)

def main():
    count()

main()

'''
    you can use the Counter against any iterable or mapping, 
    so you don’t have to just use strings.
'''