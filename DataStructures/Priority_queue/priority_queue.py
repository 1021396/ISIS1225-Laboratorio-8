from DataStructures.List import array_list as lt
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Priority_queue import index_pq_entry as pqe


def new_heap(is_min_pq=True):
    lista = lt.new_list()
    lt.add_last(lista, None)
    
    
    if is_min_pq == True:
        
        heap = {"elements": lista,
                "size": 0,
                "cmp_function":default_compare_lower_value}
        
    else: 
        heap = {"elements": lista,
                "size": 0,
                "cmp_function": default_compare_higher_value}
        
        
    return heap
        
                
def default_compare_higher_value(father_node, child_node):
    if pqe.get_key(father_node) >= pqe.get_key(child_node):
        return True
    return False


def default_compare_lower_value(father_node, child_node):
    if pqe.get_key(father_node) <= pqe.get_key(child_node):
        return True
    return False


def priority(my_heap, parent, child):
    return my_heap["cmp_function"](parent, child)


def insert(my_heap, value, key):
    pareja = pqe.new_pq_entry(key, value)
    
    lt.add_last(my_heap["elements"], pareja)
    
    my_heap['size'] += 1
    
    swim(my_heap, my_heap['size'])
    
    return my_heap


def swim(my_heap, pos):
    lista = my_heap['elements']
    centinel = True
    while pos > 1 and centinel:
        pos_padre = pos// 2
        if priority(my_heap, lista['elements'][pos_padre], lista['elements'][pos]):
            centinel = False
        else:
            lt.exchange(lista, pos_padre, pos)
            pos = pos_padre    
            

def size(my_heap):
    return my_heap['size']


def is_empty(my_heap):
    return size(my_heap) == 0


def get_first_priority(my_heap):
    if is_empty(my_heap):
        return None
    lista = my_heap['elements']
    node = lt.get_element(lista, 1)
    return pqe.get_value(node)


def remove(my_heap):
    if is_empty(my_heap):
        return None
    lista = my_heap['elements']
    lt.exchange(lista, 1, size(my_heap))
    removed = lista['elements'].pop()
    my_heap['size'] -= 1
    sink(my_heap, 1)
    return pqe.get_value(removed)


def sink(my_heap, pos):
    lista = my_heap['elements']
    size_h = size(my_heap)
    centinel = True
    while 2 * pos <= size_h and centinel:
        hijo_izq = 2 * pos
        hijo_der = 2 * pos + 1
        
        max_hijo = hijo_izq
        if hijo_der <= size_h and priority(my_heap, lista['elements'][hijo_der], lista['elements'][hijo_izq]):
            max_hijo = hijo_der
        
        if priority(my_heap, lista['elements'][pos], lista['elements'][max_hijo]):
            centinel = False
        else:
            lt.exchange(lista, pos, max_hijo)
            pos = max_hijo
        
def del_min(my_heap):
    return remove(my_heap)
