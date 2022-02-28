import time
import pickle

entry = {}
entry['title']='Dive into history, 2009 edition'
entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
entry['comments_link'] = None
entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
print(entry)

entry['published'] = True
entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')

print (entry['published_date'])

# you save the object to the disk
with open('entry.pickle', 'wb') as f:
    pickle.dump(entry, f)

# load from the file
with open('entry.pickle', 'rb') as f:
    entry = pickle.load(f)

print(entry)

# dump the pickle into the memory as a bytes object
objectMem = pickle.dumps(entry)

# load from the memory
entry2 = pickle.loads(objectMem)
print(entry==entry2)
print(entry is entry2)

'''
    pickle allows you to serialize an object and read it later
    The “==” operator compares the value or equality of two objects, 
    whereas the Python “is” operator checks whether two variables point 
    to the same object in memory.

    JSON has an array type, which the json module maps to a Python list, 
    but it does not have a separate type for “frozen arrays” (tuples). 
    And while json supports strings quite nicely, it has no support for 
    bytes objects or byte arrays.
'''