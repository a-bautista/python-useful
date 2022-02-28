from collections import namedtuple

# named tuple for creating an object
Parts = namedtuple('Parts','id_num desc cost amount')
auto_parts = Parts(id_num='1234', desc='Ford Engine', cost=1200, amount=10)
print(auto_parts.id_num)
# object
print(type(auto_parts))

auto_parts2 = ('1234', 'Ford Engine', 1200.00, 10)
print (auto_parts2[2] ) # access the cost
#1200.0

id_num, desc, cost, amount = auto_parts2
print (id_num )
#'1234'