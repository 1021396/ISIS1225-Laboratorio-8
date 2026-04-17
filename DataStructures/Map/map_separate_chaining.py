from . import map_entry as me
from . import map_functions as mf
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
import random

def new_map(num_elements, load_factor= 4, prime=109345121):
    capacity = (num_elements//load_factor) if mf.is_prime(num_elements//load_factor) else mf.next_prime((num_elements//load_factor))
    table = al.new_list()
    for i in range (0, capacity):
        list = sl.new_list()
        al.add_last(table, list)
        
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
    pair = {'key': key, 'value': value}
    list = al.get_element(my_map['table'], hash_value)
    pos = sl.is_present(list, key, default_compare)
    if pos == -1:
        my_map['size'] += 1
        sl.add_first(list, pair)
    else:
        sl.change_info(list, pos, pair)
    my_map['current_factor'] = my_map['size'] / my_map['capacity']
    
    if my_map['current_factor'] > my_map['limit_factor']:
        rehash(my_map)

    return my_map


def default_compare(key, element):

   if (key == me.get_key(element)):
      return 0
   elif (key > me.get_key(element)):
      return 1
   return -1


def contains(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    list = al.get_element(my_map['table'], hash_value)
    if sl.is_present(list, key, default_compare) == -1:
        return False
    
    return True


def remove(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    list = al.get_element(my_map['table'], hash_value)
    pos = sl.is_present(list, key, default_compare)
    if pos == -1:
        return my_map
    sl.delete_element(list, pos)
    my_map['size'] -= 1
    
    return my_map


def get(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    list = al.get_element(my_map['table'], hash_value)
    pos = sl.is_present(list, key, default_compare)
    if pos == -1:
        return None
    else:
        return me.get_value(sl.get_element(list, pos))
    

def size(my_map):
    return my_map['size']


def is_empty(my_map):
    return size(my_map) == 0


def key_set(my_map):
    keys = al.new_list()
    for list in my_map['table']['elements']:
        if not sl.is_empty(list):
            node = list['first']
            while node != None:
                al.add_last(keys, me.get_key(node['info']))
                node = node['next']
    return keys


def value_set(my_map):
    values = al.new_list()
    for list in my_map['table']['elements']:
        if not sl.is_empty(list):
            node = list['first']
            while node != None:
                al.add_last(values, me.get_value(node['info']))
                node = node['next']
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
           