def new_list():
    new_list = {
        'elements' : [],
        'size' : 0,
    }
    
    return new_list

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False
    
    
def get_element(my_list, index):
    return my_list["elements"][index]


def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def size(my_list):
    return my_list['size']

def add_first(my_list, element):
    
    if my_list['size'] == 0:
        my_list["elements"].append(element)
        my_list['size'] += 1
        
    else: 
        my_list["elements"].insert(0 ,element)
        my_list["size"] += 1
        
    return my_list
        

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list


def first_element(my_list):
    
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range') 
    
    return my_list["elements"][0]

    
def last_element(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range') 
    
    tamaño = my_list["size"]-1
    return my_list["elements"][tamaño]

    
def get_element(my_list, pos):
    if pos < 0 or pos > my_list["size"]:
        raise Exception('IndexError: list index out of range') 
    return my_list["elements"][pos]


def delete_element(my_list, pos):
    if pos < 0 or pos > my_list["size"]:
        raise Exception('IndexError: list index out of range') 
    my_list["elements"].pop(pos)
    my_list["size"]-=1
        
    return my_list

        
def remove_first(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    
    elemento = my_list["elements"].pop(0)
    my_list["size"]-=1
    return elemento

        
def remove_last(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    
    ultimo = my_list["size"]-1
    elemento = my_list["elements"].pop(ultimo)
    my_list["size"]-=1
    return elemento
        
        
def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list["size"]:
        raise Exception('IndexError: list index out of range') 
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list

def cmp_function(elemen_1, element_2):

   if elemen_1 > element_2:
      return 1
   elif elemen_1 < element_2:
      return -1
   return 0

def change_info(my_list, pos, new_info):
    
    if pos < 0 or pos > my_list["size"]:
        raise Exception('IndexError: list index out of range') 
    my_list["elements"][pos] = new_info
    return my_list

    
def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 > my_list["size"]:
        raise Exception('IndexError: list index out of range') 
    if pos2 < 0 or pos2 > my_list["size"]:
        raise Exception('IndexError: list index out of range') 
    element1 = my_list["elements"][pos1]
    element2 = my_list["elements"][pos2]
    my_list["elements"][pos1]=element2
    my_list["elements"][pos2]=element1
    return my_list
        
        
def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i > my_list["size"]:
        raise Exception('IndexError: list index out of range') 
    info = my_list["elements"][pos_i:pos_i+num_elements]
    nueva_lista = new_list()
    nueva_lista["elements"] = info
    nueva_lista["size"] = num_elements
    return nueva_lista
    
    
def default_sort_criteria(element_1, element_2):
    is_sorted = False
    
    if element_1 < element_2:
        is_sorted = True
        
    return is_sorted


def selection_sort (my_list, sort_crit):
    if is_empty(my_list):
        return my_list

    
    size_f = size(my_list)
    menor = my_list["elements"][0]
    pos_menor = 0
     
    for j in range(0,size_f):   
        for i in range(1,size_f):
            if sort_crit(my_list["elements"][i], menor):
                menor = my_list["elements"][i]
                pos_menor = i
        exchange(my_list, j, pos_menor ) 
        
    return my_list


def shell_sort(my_list, sort_crit):
    size_f = size(my_list)
    
    h = select_h(size_f)
    
    while h > 0:
        for i in range(h, size_f):
            j = i
            while j >= h:
                elem1 = get_element(my_list, j)
                elem2 = get_element(my_list, j - h)
                if sort_crit(elem1, elem2):
                    exchange(my_list, j, j - h)
                j -= h
        h = (h-1)//3
    return my_list
    
    
def select_h(size_f):
    obj = size_f // 3
    h = 1
    while h < obj:
        h = h * 3 + 1
    
    return h
                
def insertion_sort(my_list, sort_crit):
 
    if is_empty(my_list):
        return my_list

    size_f = size(my_list)

    for i in range(1, size_f):
        key = get_element(my_list, i)
        j = i - 1

        while j >= 0 and sort_crit(key, my_list["elements"][j]):
            exchange(my_list, j + 1, j)
            j -= 1

    return my_list      


def merge_sort(my_list, sort_crit):
    size_ = size(my_list)
    if size_ < 2:
        return my_list
    else:
        merge_sort_recursive(my_list, sort_crit, 0, size_ - 1)
    return my_list


def merge_sort_recursive(lst, sort_crit, lo, hi):
    if lo >= hi:
        return lst
    mid = (lo + hi) // 2
    merge_sort_recursive(lst, sort_crit, lo, mid)
    merge_sort_recursive(lst, sort_crit, mid + 1, hi)
    merge(lst, sort_crit, lo, mid, hi)


def merge(lst, sort_crit, lo, pos_mid, hi):
    i = lo
    j = pos_mid + 1
    aux_lst = new_list()
    
    while i <= pos_mid and j <= hi:
        elem1 = get_element(lst, i)
        elem2 = get_element(lst, j)
        if sort_crit(elem1, elem2):
            add_last(aux_lst, elem1)
            i += 1
        else:
            add_last(aux_lst, elem2)
            j += 1
            
    while i <= pos_mid:
        add_last(aux_lst, (get_element(lst, i)))
        i += 1
        
    while j <= hi:
        add_last(aux_lst, (get_element(lst, j)))
        j += 1
        
    k = lo
    h = 0
    while k <= hi:
        change_info(lst, k, get_element(aux_lst, h))
        k += 1
        h += 1

    return lst


def quick_sort(my_list, sort_crit):
    size_ = size(my_list)
    if size_ < 2:
        return my_list
    else:
        quick_sort_recursive(my_list, sort_crit, 0, size_ - 1)
    
    return my_list


def quick_sort_recursive(lst, sort_crit, lo, hi):
    if lo < hi:
        pivot = partition(lst, sort_crit, lo, hi)
        quick_sort_recursive(lst, sort_crit, lo, pivot - 1)
        quick_sort_recursive(lst, sort_crit, pivot + 1, hi)
    

def partition(lst, sort_crit, lo, hi):
    pivot = get_element(lst, lo)
    i = lo - 1
    j = hi + 1
    while i < j:
        i += 1
        while sort_crit(get_element(lst, i), pivot) and i < j:
            i += 1
        j -= 1
        while sort_crit(pivot, get_element(lst, j)) and i < j:
            j -= 1  
        exchange(lst, i, j)

    
    if j <= i :
        exchange(lst, lo, j)
    
    return j
        
def sort_criteria1(e1, e2):
    if e1["timestamp"] == e2["timestamp"]:
        return e1["event_id"] < e2["event_id"]
    return e1["timestamp"] < e2["timestamp"]
