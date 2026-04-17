from DataStructures.List import single_linked_list as al
from DataStructures.Tree import bst_node as bst
from DataStructures.List import single_linked_list as sl

def new_map():
    binary_search_tree = {"root":None}
    return binary_search_tree

def size(my_bst):
    tamaño = size_tree(my_bst["root"])
    return tamaño
def size_tree(root):
    if root is None:
        return 0
    else:
        return root["size"]
    
def get_node(node,key):
    if node is None:
        return None
    else:
        if key == node["key"]:
            return node["value"]
        if key < node["key"]:
            return get_node(node["left"],key)
        else:
            return get_node(node["right"],key)

def get(bst, key):
    """
    Buscar la key en el BST.
    Retornar el value de la key (si la key existe). None de lo contrario.
    """
    value = get_node(bst['root'], key)
    return value           


def insert_node(node,key,value):
    if node is None:
        return bst.new_node(key,value)
    
    comparacion = default_compare(key,node)
    
    if comparacion == 0:
        node["value"] = value
        return node
    if comparacion == -1:
         node["left"] = insert_node(node["left"],key,value)

    if comparacion == 1:
         node["right"] = insert_node(node["right"],key,value)
         
    peso_izq = size_tree(node["left"])
    peso_der = size_tree(node["right"])
    node["size"] = peso_izq + peso_der + 1
    
    return node

def put(bst, key, value):
    """
    gregar la pareja key-value en el BST manteniendo el orden.
    Si la key existe, el value se reemplaza.
    Retornar el BST resultante con el nuevo nodo (o el nodo actualizado con el
    value reemplazado).
    """
    bst['root'] = insert_node(bst['root'], key, value )
    return bst

def default_compare(key, element):
   if key == bst.get_key(element):
      return 0
   elif key > bst.get_key(element):
      return 1
   return -1

def contains(my_bst, key):
    existe = get(my_bst,key)
    if existe is not None:
        return True
    else:
        return False

def is_empty(my_bst):
    if my_bst["root"] is None:
        return True
    else:
        return False
    
    


def key_set(my_bst):
    lista = sl.new_list()
    keyset = key_set_tree(my_bst["root"],lista)
    return keyset

def key_set_tree(root,key_list):
    if root is not None:
        key_set_tree(root["left"],key_list)
        sl.add_last(key_list,root["key"])
        key_set_tree(root["right"],key_list)
    return key_list
    

def value_set(my_bst):
    lista = sl.new_list()
    keyset = key_set_tree(my_bst["root"],lista)
    return keyset

def value_set_tree(root,key_list):
    if root is not None:
        key_set_tree(root["left"],key_list)
        sl.add_last(key_list,root["value"])
        key_set_tree(root["right"],key_list)
    return key_list


def get_min(my_bst):
    if my_bst["root"] is None:
        return None
    minimo = get_min_node(my_bst["root"])
    return minimo
    
    
def get_min_node(root):
    if root["left"] is None:
        return root["key"]
    else:
        return get_min_node(root["left"])


def get_max(my_bst):
    if my_bst["root"] is None:
        return None
    minimo = get_min_node(my_bst["root"])
    return minimo
    
    
def get_max_node(root):
    if root["right"] is None:
        return root["key"]
    else:
        return get_min_node(root["right"])
    



def delete_min(my_bst):
    my_bst['root'] = del_min_tree(my_bst['root'])
    return my_bst

def del_min_tree(root):
    if root == None:
        return None
    if root['left'] == None:
        return root['right']
    else:
        root['size'] -= 1
        del_min_tree(root['left'])
        return root

def delete_max(my_bst):
    my_bst['root'] = del_max_tree(my_bst['root'])
    return my_bst

def del_max_tree(root):
    if root == None:
        return None
    if root['right'] == None:
        return root['left']
    else:
        root['size'] -= 1
        del_min_tree(root['right'])
        return root

def height_tree(root):

    if root is None:
        return 0
    else:
        left_height = height_tree(root["left"])
        right_height = height_tree(root["right"])
        return 1 + max(left_height, right_height)

def height(my_bst):
    
    return height_tree(my_bst["root"])

def keys(my_bst, key_initial, key_final):
   
    lista_llaves = al.new_list()
    return keys_range(my_bst["root"], key_initial, key_final, lista_llaves)

      
def keys_range(root, key_initial, key_final, list_key):
    
    if root is None:
        return list_key

    if key_initial <= root["key"] <= key_final:
        
        keys_range(root["left"], key_initial, key_final, list_key)
        al.add_last(list_key,root["key"])
        
        keys_range(root["right"], key_initial, key_final, list_key)
    elif root["key"] < key_initial:
        
        keys_range(root["right"], key_initial, key_final, list_key)
    else:  
        
        keys_range(root["left"], key_initial, key_final, list_key)

    return list_key

def values(my_bst, key_initial, key_final):
    
    lista_llaves = al.new_list()
    return value_range(my_bst["root"], key_initial, key_final, lista_llaves)

      
def value_range(root, key_initial, key_final, list_key):
    
    if root is None:
        return list_key

    if key_initial <= root["key"] <= key_final:
        
        value_range(root["left"], key_initial, key_final, list_key)
        al.add_last(list_key, root["value"])
    
        value_range(root["right"], key_initial, key_final, list_key)
    elif root["key"] < key_initial:
        
        value_range(root["right"], key_initial, key_final, list_key)
    else:  
        value_range(root["left"], key_initial, key_final, list_key)

    return list_key
