from DataStructures.List import list_node as nd

def new_list():
    new_list = {
        "first": None,
        "last": None,
        "size": 0
    }
    
    return new_list


def is_empty(my_list):
    if size(my_list) == 0:
        return True
    
    return False


def size(my_list):
    return my_list['size']


def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    
    if pos == 0:
        return add_first(my_list, element)
    elif pos == size(my_list) :
        return add_last(my_list, element)
    
    new_node = nd.new_single_node(element)
    node = my_list['first']
    searchpos = 0
    while searchpos < pos-1:
        node = node['next']
        searchpos += 1
        
    new_node['next'] = node['next']
    node['next'] = new_node
    my_list['size'] += 1
    
    return my_list


def add_first(my_list, element):
    new_node = nd.new_single_node(element)
    
    if is_empty(my_list):
        my_list['first'] = new_node
        my_list['last'] = new_node
    else:
        new_node['next'] = my_list['first']
        my_list['first'] = new_node
        
    my_list['size'] += 1
    
    return my_list


def add_last(my_list, element):
    new_node = nd.new_single_node(element)
    
    if is_empty(my_list):
        my_list['first'] = new_node
        my_list['last'] = new_node
    else:
        my_list['last']['next'] = new_node
        my_list['last'] = new_node
        
    my_list['size'] += 1
    
    return my_list


def first_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    
    return nd.get_element(my_list['first'])


def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    
    return nd.get_element(my_list['last'])
        

def get_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    searchpos = 0
    node = my_list['first']
    while searchpos < pos:
        node = node['next']
        searchpos += 1
    
    return nd.get_element(node)


def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    if size(my_list) == 1:
        my_list['first'] = None
        my_list['last'] = None
        
    elif pos == 0:
        my_list['first'] = my_list['first']['next'] 
           
    elif pos == size(my_list) - 1:
        searchpos = 0
        node = my_list['first']
        while searchpos < size(my_list) - 2:
            node = node['next']
            searchpos += 1
        node['next'] = None
        my_list['last'] = node  
        
    else:
        searchpos = 0
        node = my_list['first']
        while searchpos < pos - 1:
            node = node['next']
            searchpos += 1
        node['next'] = node['next']['next']
        
    my_list['size'] -= 1
    
    return my_list          
            
            
def remove_first(my_list):
    if size(my_list) == 0:
        raise Exception('IndexError: list index out of range')
    
    removed_info = nd.get_element(my_list['first'])
    if size(my_list) == 1:
        my_list['first'] = None
        my_list['last'] = None
    else:
        my_list['first'] = my_list['first']['next']
        
    my_list['size'] -= 1    
    
    return removed_info
    
    
def remove_last(my_list):
    if size(my_list) == 0:
        raise Exception('IndexError: list index out of range')
    
    removed_info = nd.get_element(my_list['last'])
    if size(my_list) == 1:
        my_list['first'] = None
        my_list['last'] = None
    else:
        searchpos = 0
        node = my_list['first']
        while searchpos < size(my_list) - 2:
            node = node['next']
            searchpos += 1
        node['next'] = None
        my_list['last'] = node
    my_list['size'] -= 1    
    
    return removed_info


def cmp_function(element_1, element_2):

   if element_1 > element_2:
      return 1
   elif element_1 < element_2:
      return -1
   return 0
    

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list['first']
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp['info']) == 0:
            is_in_array = True
        else:
            temp = temp['next']
            count += 1
            
    if not is_in_array:
        count = -1
        
    return count


def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    searchpos = 0
    node = my_list['first']
    while searchpos < pos:
        node = node['next']
        searchpos += 1
    node['info'] = new_info
    return my_list


def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 >= size(my_list) or pos2 < 0 or pos2 >= size(my_list):
        raise Exception('IndexError: list index out of range')
    
    if pos1 == pos2:
        return my_list
    
    if pos1 > pos2:
        pos1, pos2 = pos2, pos1
       
    node1 = my_list['first']
    prev1 = None
    searchpos1 = 0
    while searchpos1 < pos1:
        prev1 = node1
        node1 = node1['next']
        searchpos1 += 1
    
    node2 = my_list['first']
    prev2 = None    
    searchpos2 = searchpos1
    while searchpos2 < pos2:
        prev2 = node2
        node2 = node2['next']
        searchpos2 += 1
    
    if prev2 == node1:  
        node1['next'] = node2['next']
        node2['next'] = node1
        if prev1:
            prev1['next'] = node2
        else:
            my_list['first'] = node2
    else:
        if prev1:
            prev1['next'] = node2
        else:
            my_list['first'] = node2

        if prev2:
            prev2['next'] = node1
        else:
            my_list['first'] = node1

        node1['next'], node2['next'] = node2['next'], node1['next']

    if node1['next'] is None:
        my_list['last'] = node1
    elif node2['next'] is None:
        my_list['last'] = node2

    return my_list


def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos + num_elements> size(my_list):
        raise Exception('IndexError: list index out of range')
    
    sub_list = new_list()
    sub_list['size'] = num_elements
    
    searchpos = 0
    node = my_list['first']
    while searchpos < pos:
        node = node['next']
        searchpos += 1
    first_node = node.copy()
    sub_list['first'] = first_node
    
    i = 1
    while i < num_elements:
        node = node['next']
        i += 1
    last_node = node.copy()
    sub_list['last'] = last_node
    sub_list['last']['next'] = None
    
    return sub_list


def default_sort_criteria(element_1, element_2):
    is_sorted = False
    
    if element_1 < element_2:
        is_sorted = True
        
    return is_sorted


def selection_sort (my_list, sort_crit):
    if is_empty(my_list):
        return my_list
    
    for i in range(size(my_list)-1):
        minimo = get_element(my_list, i)
        pos_min = 0
        for j in range(i+1, size(my_list)):
            if sort_crit(get_element(my_list,j), minimo):
                minimo = get_element(my_list,j)
                pos_min = j
            exchange(my_list, i, pos_min)
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

    for i in range(1, size(my_list)):
        key = get_element(my_list, i)
        j = i - 1

        while j >= 0 and sort_crit(key, get_element(my_list, j)):
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