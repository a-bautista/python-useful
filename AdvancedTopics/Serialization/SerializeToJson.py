import pickle
import json
import time

def to_json(python_object):  
    print(type(python_object))                     
    if isinstance(python_object, time.struct_time):
        return {'__class__': 'time.asctime',
                '__value__': time.asctime(python_object)}

    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': list(python_object)}

    raise TypeError(repr(python_object) + ' is not JSON serializable')

def from_json(json_object):                                  
    if '__class__' in json_object:                           
        if json_object['__class__'] == 'time.asctime':
            return time.strptime(json_object['__value__'])   
        if json_object['__class__'] == 'bytes':
            return bytes(json_object['__value__'])          
    return json_object

def main():
    # load from the file
    with open('entry.pickle', 'rb') as f:
        entry = pickle.load(f)
    
    # print(entry['published_date'])
    # print(type(entry['published_date']))
    # print(entry)
    # dump the pickle to a json
    with open('entry.json', 'w', encoding='utf-8') as f:
        json.dump(entry, f, indent=4, default=to_json)
    
    # serialize the json to an object in memory
    with open('entry.json', 'r', encoding='utf-8') as f:
        entry2 = json.load(f, object_hook=from_json)

    print(entry2)

main()

'''
    There's a bug, the time struct won't be converted.
'''
