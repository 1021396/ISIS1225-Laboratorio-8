from . import map_entry as me
from . import map_functions as mf
from DataStructures.List import array_list as al
import random

def new_map(num_elements, load_factor, prime=109345121):
    capacity = (num_elements//load_factor) if mf.is_prime(num_elements//load_factor) else mf.next_prime((num_elements//load_factor))
    table = al.new_list()
    for i in range (0, capacity):
        pair = {'key': None,
                'value': None}
        al.add_last(table, pair)
        
    new_map = {'prime': prime,
               'capacity': capacity,
               'scale': random.randint(1, prime - 1),
               'shift': random.randint(0, prime - 1),
               'table': table,
               'current_factor': 0,
               'limit_factor': load_factor,
               'size': 0}
    
    return new_map


def put(my_map, key, value):
    hash_value = mf.hash_value(my_map, key)  
    ocupied, slot = find_slot(my_map, key, hash_value)

    pair = al.get_element(my_map['table'], slot)
    me.set_key(pair, key)
    me.set_value(pair, value)
    
    if not ocupied:
        my_map['size'] += 1
        my_map['current_factor'] = my_map['size'] / my_map['capacity']
        if my_map['current_factor'] > my_map['limit_factor']:
            rehash(my_map)

    return my_map
       
    
def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail


def is_available(table, pos):

   entry = al.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False


def default_compare(key, entry):
    if key == me.get_key(entry):
      return 0
    elif key > me.get_key(entry):
      return 1
    return -1


def contains(my_map, key):
    if size(my_map) == 0:
        return False
    
    hash_value = mf.hash_value(my_map, key)
    ocupied, slot = find_slot(my_map, key, hash_value)
    return ocupied
        
        
def get(my_map, key):
    
    if size(my_map) == 0:
        return None
    
    hash_value = mf.hash_value(my_map, key)
    ocupied, slot = find_slot(my_map, key, hash_value)
    if ocupied:
        return me.get_value(al.get_element(my_map['table'], slot))
    else:
        return None


def remove(my_map, key):   
    hash_value = mf.hash_value(my_map, key)
    ocupied, slot = find_slot(my_map, key, hash_value)
    if not ocupied:
        return my_map
    
    pair = al.get_element(my_map['table'], slot)       
    me.set_key(pair, None)
    me.set_value(pair, None)
    my_map['size'] -= 1
    
    return my_map


def size(my_map):
    return my_map['size']


def is_empty(my_map):
    return size(my_map) == 0


def key_set(my_map):
    keys = al.new_list()
    for i in range(al.size(my_map['table'])):
        pair = al.get_element(my_map['table'], i)
        key = me.get_key(pair)
        if key is not None:
            al.add_last(keys, key)
            
    return keys


def value_set(my_map):
    values = al.new_list()
    for i in range(al.size(my_map['table'])):
        pair = al.get_element(my_map['table'], i)
        value = me.get_value(pair)
        if value is not None:
            al.add_last(values, value)
            
    return values
            

def rehash(my_map):
    
    if is_empty(my_map):
        return my_map
    
    actual_capacity = my_map['capacity']
    num_elements = (2*actual_capacity) * my_map['limit_factor']
    new = new_map(num_elements, my_map['limit_factor'])

    keys = key_set(my_map)  
    values = value_set(my_map) 

    for i in range(al.size(keys)):
        put(new, al.get_element(keys, i), al.get_element(values, i))

    my_map['prime'] = new['prime']
    my_map['capacity'] = new['capacity']
    my_map['scale'] = new['scale']
    my_map['shift'] = new['shift']
    my_map['table'] = new['table']
    my_map['current_factor'] = new['current_factor']
    my_map['limit_factor'] = new['limit_factor']
    my_map['size'] = new['size']

    return my_map
    