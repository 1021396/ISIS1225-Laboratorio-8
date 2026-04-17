def new_stack():
    return {"first": None, "last": None, "size": 0}

def new_node(info):
    return {"info": info, "next": None}

def pop (stack):
    if stack["size"]==0:
        return None
    elif stack["size"]==1:
        ultimo = stack["last"]["info"]
        stack["first"]=None
        stack["last"]=None
        stack["size"]=0
        return ultimo
    else:
        ultimo=stack["last"]["info"]
        current=stack["first"]
        for _ in range (stack["size"]-2):
            current=current["next"]
        current["next"]=None
        stack["last"]=current
        stack["size"]-=1
        return ultimo

def push (stack, element):
    nodo=new_node(element)
    if stack["size"]==0:
        stack["first"]=nodo
        stack["last"]=nodo
        stack["size"]=1
    else:
        ultimo=stack["last"]
        ultimo["next"]=nodo
        stack["last"]=nodo
        stack["size"]+=1
    return stack

def is_empty (stack):
    return stack["size"]==0

def size (stack):
    return stack["size"]

def top (stack):
    if stack["size"]==0:
        return None
    else:
        return stack["last"]["info"]