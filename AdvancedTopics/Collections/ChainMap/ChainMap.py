from collections import ChainMap

car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options = {'A/C':1000, 'Turbo':2500, 'rollbar':300}

car_pricing = ChainMap(car_options, car_parts)
print(car_pricing['Turbo'])