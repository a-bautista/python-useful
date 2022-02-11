from collections import OrderedDict

d = {'banana': 3, 'apple':4, 'pear': 7, 'orange': 10}
new_d = OrderedDict()

new_d['apple'] = d['apple']
new_d['pear'] = d['pear']
new_d['orange'] = d['orange']
new_d['banana'] = d['banana']

print(new_d)

new_d = OrderedDict(sorted(d.items()))
print(new_d)
new_d.popitem()
print(new_d)
new_d.move_to_end('apple')
print(new_d)